import random
import tkinter as tk
from tkinter import ttk, messagebox


# --- GLOBAL CONFIGURATION ---
LILITA = "Lilita One"
BG_COLOR = "#1D61BB"
EXIT_COLOR = "#D32F2F"
BACK_COLOR = "#4CAF50"


ATTENDANCE_FACTS = [
   "Missing 10% of the school year impacts academic advancement.",
   "Regular attendance correlates with higher tertiary achievements.",
   "Every day missed affects your final subject credit potential.",
   "Arriving late disrupts concentration and classroom flow.",
   "Strong attendance builds essential workplace habits."
]




class AttendanceApp:
   def __init__(self, root):
       self.root = root
       self.root.geometry("1000x600")
       try:
           self.root.option_add("*Font", (LILITA, 12))
       except:
           self.root.option_add("*Font", ("Arial", 12))


       self.container = tk.Frame(root, bg=BG_COLOR)
       self.container.pack(fill="both", expand=True)
       self.show_page(LoginPage)


   def show_page(self, page_class, data=None):
       for widget in self.container.winfo_children():
           widget.destroy()
       if data is not None:
           page_class(self.container, self, data)
       else:
           page_class(self.container, self)




# --- NAVIGATION HELPER ---
def add_nav(frame, app, back_page=None):
   if back_page:
       tk.Button(frame, text="BACK", bg=BACK_COLOR, fg="white",
                 command=lambda: app.show_page(back_page)).place(x=30, y=540)
   tk.Button(frame, text="EXIT", bg=EXIT_COLOR, fg="white",
             command=app.root.quit).place(x=920, y=540)




# --- PAGES ---
class LoginPage:
   def __init__(self, frame, app):
       tk.Label(frame, text="LOGIN PAGE", font=(LILITA, 36), bg=BG_COLOR, fg="white").pack(pady=50)
       self.name_var = tk.StringVar()
       self.name_var.trace_add("write", self.validate)
       self.ent = tk.Entry(frame, textvariable=self.name_var, font=(LILITA, 14))
       self.ent.pack(pady=20)
       self.feedback_lbl = tk.Label(frame, text="", bg=BG_COLOR, fg="#FFC107")
       self.feedback_lbl.pack()
       self.enter_btn = tk.Button(frame, text="ENTER", bg="#FFC107", fg="black", font=(LILITA, 14),
                                  state="disabled", command=lambda: app.show_page(HomePage))
       self.enter_btn.pack(pady=20)
       tk.Button(frame, text="EXIT", bg=EXIT_COLOR, fg="white", font=(LILITA, 12), command=app.root.quit).place(x=920,
                                                                                                                y=540)


   def validate(self, *args):
       val = self.name_var.get()
       if val.isalpha() and len(val) >= 2:
           self.enter_btn.config(state="normal")
           self.feedback_lbl.config(text="Valid name!", fg="#7ED957")
       else:
           self.enter_btn.config(state="disabled")
           self.feedback_lbl.config(text="Name must have at least two letters and only letters!", fg="#FFFF00")




class HomePage:
   def __init__(self, frame, app):
       tk.Label(frame, text="ATTENDANCE ANALYTICS", font=(LILITA, 36), bg=BG_COLOR, fg="white").pack(pady=50)
       btn_style = {"bg": "#FFC107", "fg": "black", "font": (LILITA, 14), "width": 20, "height": 2}
       tk.Button(frame, text="CALCULATOR", **btn_style, command=lambda: app.show_page(CalculatorPage)).pack(pady=10)
       tk.Button(frame, text="FAQ", **btn_style, command=lambda: app.show_page(FaqPage)).pack(pady=10)
       tk.Button(frame, text="FACTS", **btn_style, command=lambda: app.show_page(FactsPage)).pack(pady=10)
       add_nav(frame, app, None)




class CalculatorPage:
   def __init__(self, frame, app):
       self.frame = frame
       self.app = app
       tk.Label(frame, text="ATTENDANCE CALCULATOR", font=(LILITA, 28), bg=BG_COLOR, fg="white").pack(pady=20)
       self.tree = ttk.Treeview(frame, columns=("Subject", "Attended", "Total", "Desired", "Percentage"),
                                show="headings", height=8)
       for col in ["Subject", "Attended", "Total", "Desired", "Percentage"]:
           self.tree.heading(col, text=col)
           self.tree.column(col, width=120)
       self.tree.pack(pady=10)


       input_f = tk.Frame(frame, bg="#E7B96D", padx=15, pady=15)
       input_f.pack(pady=5)
       self.s, self.a, self.t, self.d = [tk.Entry(input_f, width=10) for _ in range(4)]
       for e in [self.s, self.a, self.t, self.d]: e.pack(side="left", padx=5)


       tk.Button(input_f, text="+", command=self.add_row).pack(side="left", padx=5)
       tk.Button(input_f, text="-", command=self.remove_latest_row).pack(side="left", padx=5)
       self.action_btn = tk.Button(frame, text="CALCULATE", bg="#FFC107", fg="black", font=(LILITA, 14),
                                   command=self.calculate)
       self.action_btn.pack(pady=20)
       add_nav(frame, app, HomePage)


   def add_row(self):
       self.tree.insert("", "end", values=(self.s.get(), self.a.get(), self.t.get(), self.d.get(), ""))


   def remove_latest_row(self):
       children = self.tree.get_children()
       if children: self.tree.delete(children[-1])


   def calculate(self):
       for item in self.tree.get_children():
           try:
               vals = self.tree.item(item, 'values')
               perc = (float(vals[1]) / float(vals[2])) * 100
               self.tree.set(item, column="Percentage", value=f"{perc:.1f}%")
           except:
               self.tree.set(item, column="Percentage", value="Error")
       self.action_btn.config(text="CHECK ANALYTICS", command=self.go_to_analytics)


   def go_to_analytics(self):
       # FIX: Collect ALL 4 raw inputs instead of just Sub and Percentage string
       results = []
       for i in self.tree.get_children():
           v = self.tree.item(i, 'values')
           results.append((v[0], float(v[1]), float(v[2]), float(v[3])))
       self.app.show_page(AnalyticsPage, data=results)




class AnalyticsPage:
   def __init__(self, frame, app, data=None):
       tk.Label(frame, text="PREDICTIVE ANALYTICS", font=(LILITA, 28), bg=BG_COLOR, fg="white").pack(pady=20)
       df = tk.Frame(frame, bg="#E7B96D", padx=20, pady=20)
       df.pack(fill="x", padx=50)


       if data:
           for sub, attended, total, desired in data:
               current_perc = (attended / total) * 100
               row_f = tk.Frame(df, bg="#E7B96D")
               row_f.pack(fill="x", pady=5)


               if current_perc >= desired:
                   msg = "Minimum Met!"
                   color = "#7ED957"
               else:
                   # Mathematical formula for consecutive days needed to reach threshold
                   needed = ((desired * total) - (attended * 100)) / (100 - desired)
                   msg = f"Need {int(needed) + 1} more days"
                   color = "#D32F2F"
               tk.Label(row_f, text=f"{sub}: {msg}", font=(LILITA, 14), bg=color, fg="white", padx=10).pack(fill="x")


       add_nav(frame, app, CalculatorPage)




class FaqPage:
   def __init__(self, frame, app):
       self.frame = frame
       self.app = app


       # Header
       tk.Label(frame, text="FREQUENTLY ASKED QUESTIONS", font=(LILITA, 22),
                bg=BG_COLOR, fg="white").pack(pady=20)


       # Container for the FAQ list
       self.faq_container = tk.Frame(frame, bg=BG_COLOR)
       self.faq_container.pack(expand=True, fill="both", padx=50)


       # FAQ Data
       faqs = [
           ("How is the attendance percentage calculated?",
            "It divides days attended by total academic track terms multiplied by 100."),
           ("How do I avoid lateness/truances?",
            "Try consistently leaving early to have more than enough time to arrive."),
           ("How often should I use the Predictive Analysis tool?",
            "Checking every week helps track trends before percentages drop too low.")
       ]


       # The Loop that creates the "boxed" look
       for q, a in faqs:
           # This frame acts as the background box for each Q&A
           box = tk.Frame(self.faq_container, bg="#2E66B6", padx=10, pady=8,
                          bd=1, relief="groove")
           box.pack(fill="x", pady=6)


           # The Question Label
           tk.Label(box, text=f"Q: {q}", font=("Arial", 11, "bold"),
                    bg="#2E66B6", fg="#FFC107", anchor="w").pack(fill="x")


           # The Answer Label
           tk.Label(box, text=a, font=("Arial", 10), bg="#2E66B6", fg="white",
                    wraplength=500, justify="left", anchor="w").pack(fill="x", pady=(2, 0))


       add_nav(frame, app, HomePage)




class FactsPage:
   def __init__(self, frame, app):
       tk.Label(frame, text="ATTENDANCE FACTS", font=(LILITA, 28), bg=BG_COLOR, fg="white").pack(pady=20)
       self.lbl = tk.Label(frame, text="Click to generate", bg="white", width=50, height=5)
       self.lbl.pack(pady=20)
       tk.Button(frame, text="GENERATE", command=lambda: self.lbl.config(text=random.choice(ATTENDANCE_FACTS))).pack()
       add_nav(frame, app, HomePage)




if __name__ == "__main__":
   root = tk.Tk()
   app = AttendanceApp(root)
   root.mainloop()










