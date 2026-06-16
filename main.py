import random
from tkinter import *
from PIL import Image, ImageTk


# Global application data structures to satisfy Level 3 data persistence rules
name_list = []
user_name = ""
global_background_file = "Attendance Analytics.png"


# Hardcoded list of educational attendance insights for the randomizer subsystem (9.png)
ATTENDANCE_FACTS = [
   "Missing just 10% of the school year can drastically impact academic advancement.",
   "Regular school attendance directly correlates with higher tertiary qualification achievements.",
   "Every single school day missed takes a toll on your final subject credit potential.",
   "Arriving late to classes disrupts personal concentration and overall classroom flow.",
   "Establishing strong attendance routines now builds excellent workplace habits for the future."
]




class LoginPage:
   def __init__(self, parent):
       self.parent = parent
       background_color = "#1D61BB"


       try:
           self.image = Image.open(global_background_file)
           self.photo = ImageTk.PhotoImage(self.image)
           self.img_width, self.img_height = self.image.size
       except Exception:
           # Fallback size parameters if background graphic asset is missing
           self.img_width, self.img_height = 1000, 600
           self.photo = None


       parent.geometry(f"{self.img_width}x{self.img_height}")
       parent.title("Attendance Analytics - Secure Login")


       self.login_frame = Frame(parent, bg=background_color)
       self.login_frame.pack(fill="both", expand=True)


       if self.photo:
           self.bg_label = Label(self.login_frame, image=self.photo, bd=0)
           self.bg_label.place(x=0, y=0)


       self.container = Frame(self.login_frame, bg=background_color)
       self.container.pack(expand=True)


       self.text_canvas = Canvas(self.container, width=400, height=120, bg=background_color, highlightthickness=0)
       self.text_canvas.pack(pady=0, padx=(0, 100))


       self.text_canvas.create_text(202, 90, text="NAME", font=("Lilita One", 36), fill="black")
       self.text_canvas.create_text(200, 88, text="NAME", font=("Lilita One", 36), fill="white")


       self.entry_box = Entry(self.container, width=22, font=("Lilita One", 16), justify="center")
       self.entry_box.pack(pady=22, padx=(0, 100))
       self.entry_box.bind("<KeyRelease>", self.validate_name)


       self.continue_button = Button(self.container, text="ENTER", font=("Lilita One", 14), state="disabled",
                                     command=self.name_collect)
       self.continue_button.pack(pady=0, padx=(0, 100))


       self.error_label = Label(self.container, text="", fg="red", bg=background_color, font=("Lilita One", 11))
       self.error_label.pack(pady=10, padx=(0, 100))


   def validate_name(self, event=None):
       name = self.entry_box.get().strip()
       if len(name) < 2:
           self.error_label.config(text="⚠ NAME MUST BE AT LEAST TWO LETTERS.")
           self.continue_button.config(state="disabled")
       elif not name.isalpha():
           self.error_label.config(text="⚠ NAME MUST CONTAIN ONLY LETTERS")
           self.continue_button.config(state="disabled")
       else:
           self.error_label.config(text="")
           self.continue_button.config(state="normal")


   def name_collect(self):
       global user_name
       name = self.entry_box.get().strip()
       if name:
           user_name = name
           name_list.append(name)
           self.login_frame.pack_forget()
           HomePage(self.parent)




class HomePage:
   def __init__(self, parent):
       self.parent = parent
       parent.title("Attendance Analytics - Main Hub")
       background_color = "#1D61BB"


       self.home_frame = Frame(parent, bg=background_color)
       self.home_frame.pack(fill="both", expand=True)


       try:
           self.image = Image.open(global_background_file)
           self.photo = ImageTk.PhotoImage(self.image)
           self.bg_label = Label(self.home_frame, image=self.photo, bd=0)
           self.bg_label.place(x=0, y=0)
           self.bg_label.image = self.photo
       except Exception:
           pass


       self.menu_container = Frame(self.home_frame, bg=background_color)
       self.menu_container.pack(expand=True)


       # Welcome banner mapping dynamic state variable
       self.welcome_lbl = Label(self.menu_container, text=f"WELCOME, {user_name.upper()}!", font=("Lilita One", 28),
                                bg=background_color, fg="white")
       self.welcome_lbl.pack(pady=(0, 30))


       # Functional Component Navigation Controls
       self.calc_button = Button(self.menu_container, text="CALCULATOR", font=("Lilita One", 18), bg="#FFC107",
                                 fg="black", width=22, height=2, bd=0, cursor="hand2", command=self.open_calculator)
       self.calc_button.pack(pady=12)


       self.faq_button = Button(self.menu_container, text="FAQ", font=("Lilita One", 18), bg="#FFC107", fg="black",
                                width=22, height=2, bd=0, cursor="hand2", command=self.open_faq)
       self.faq_button.pack(pady=12)


       self.facts_button = Button(self.menu_container, text="ATTENDANCE FACTS", font=("Lilita One", 18), bg="#FFC107",
                                  fg="black", width=22, height=2, bd=0, cursor="hand2", command=self.open_facts)
       self.facts_button.pack(pady=12)


       # Global system exit configuration component
       self.exit_button = Button(self.home_frame, text="EXIT", font=("Lilita One", 12), bg="#D32F2F", fg="white", bd=0,
                                 padx=15, pady=5, command=self.parent.quit)
       self.exit_button.place(x=30, y=530)


   def open_calculator(self):
       self.home_frame.pack_forget()
       CalculatorPage(self.parent)


   def open_faq(self):
       self.home_frame.pack_forget()
       FaqPage(self.parent)


   def open_facts(self):
       self.home_frame.pack_forget()
       FactsPage(self.parent)




class CalculatorPage:
   def __init__(self, parent):
       self.parent = parent
       background_color = "#1D61BB"


       self.calc_frame = Frame(parent, bg=background_color)
       self.calc_frame.pack(fill="both", expand=True)


       try:
           self.image = Image.open(global_background_file)
           self.photo = ImageTk.PhotoImage(self.image)
           self.bg_label = Label(self.calc_frame, image=self.photo, bd=0)
           self.bg_label.place(x=0, y=0)
           self.bg_label.image = self.photo
       except Exception:
           pass


       self.main_layout = Frame(self.calc_frame, bg=background_color)
       self.main_layout.pack(expand=True, pady=40)


       # Dynamic Row Creation Setup
       self.headers = ["SUBJECTS", "DAYS ATTENDED", "TOTAL DAYS", "GOAL %"]
       for col_idx, text in enumerate(self.headers):
           lbl = Label(self.main_layout, text=text, font=("Lilita One", 14), bg=background_color, fg="white", width=15)
           lbl.grid(row=0, col=col_idx, padx=5, pady=10)


       self.rows_data = []
       self.row_counter = 1
       self.add_row()  # Always start with at least one data entry line


       # Control Panel Elements Layer
       self.controls_frame = Frame(self.calc_frame, bg=background_color)
       self.controls_frame.pack(side="bottom", fill="x", pady=20)


       self.back_btn = Button(self.controls_frame, text="BACK", font=("Lilita One", 12), bg="#E0E0E0",
                              command=self.go_back)
       self.back_btn.pack(side="left", padx=30)


       self.submit_btn = Button(self.controls_frame, text="CHECK ANALYTICS", font=("Lilita One", 14), bg="#FFC107",
                                command=self.process_calculations)
       self.submit_btn.pack(side="right", padx=30)


       # Boundary Logic Counter Matrix
       self.stepper_frame = Frame(self.controls_frame, bg=background_color)
       self.stepper_frame.pack(side="bottom", pady=5)


       Label(self.stepper_frame, text="NO. OF SUBJECTS:", font=("Lilita One", 11), bg=background_color,
             fg="white").pack(side="left", padx=5)
       Button(self.stepper_frame, text="-", font=("Lilita One", 12), width=3, command=self.remove_row).pack(
           side="left")
       Button(self.stepper_frame, text="+", font=("Lilita One", 12), width=3, command=self.add_row).pack(side="left",
                                                                                                         padx=5)


   def add_row(self):
       if self.row_counter <= 5:  # Safe layout limit to prevent desktop frame clipping
           r_entries = []
           for c_idx in range(4):
               ent = Entry(self.main_layout, font=("Arial", 12), width=14, justify="center")
               ent.grid(row=self.row_counter, column=c_idx, padx=5, pady=6)
               if c_idx == 0:
                   ent.insert(0, f"Subject {self.row_counter}")
               elif c_idx == 3:
                   ent.insert(0, "85")  # Standard default benchmark
               r_entries.append(ent)
           self.rows_data.append(r_entries)
           self.row_counter += 1


   def remove_row(self):
       if len(self.rows_data) > 1:
           for ent in self.rows_data[-1]:
               ent.destroy()
           self.rows_data.pop()
           self.row_counter -= 1


   def process_calculations(self):
       calculated_results = []
       for row in self.rows_data:
           try:
               sub_name = row[0].get().strip()
               attended = float(row[1].get().strip())
               total = float(row[2].get().strip())
               goal = float(row[3].get().strip())


               if total <= 0 or attended < 0 or goal < 0:
                   continue  # Guard condition checks invalid data records cleanly


               current_pct = (attended / total) * 100
               required_days = max(0, int(((goal / 100) * total) - attended))


               calculated_results.append({
                   "subject": sub_name, "current": current_pct, "days_needed": required_days, "goal": goal
               })
           except ValueError:
               pass  # Ignore incomplete fields safely without throwing code crashes


       if calculated_results:
           self.calc_frame.pack_forget()
           AnalyticsPage(self.parent, calculated_results)


   def go_back(self):
       self.calc_frame.pack_forget()
       HomePage(self.parent)




class AnalyticsPage:
   def __init__(self, parent, results):
       self.parent = parent
       background_color = "#1D61BB"


       self.analytics_frame = Frame(parent, bg=background_color)
       self.analytics_frame.pack(fill="both", expand=True)


       # Layout Container Block
       self.center_wrapper = Frame(self.analytics_frame, bg=background_color)
       self.center_wrapper.pack(expand=True)


       title = Label(self.center_wrapper, text="PREDICTIVE PERFORMANCE PROFILE", font=("Lilita One", 20),
                     bg=background_color, fg="white")
       title.pack(pady=10)


       # Build individual analytics summary display boxes matching layout 7.png
       for data in results:
           card = Frame(self.center_wrapper, bg="#FFFFFF", padx=15, pady=10, highlightthickness=1,
                        highlightbackground="#FFC107")
           card.pack(fill="x", pady=8)


           txt_info = f"{data['subject'].upper()}: Current Attendance is {data['current']:.1f}% (Goal: {data['goal']:.0f}%)"
           Label(card, text=txt_info, font=("Arial", 11, "bold"), bg="white", fg="black").pack(anchor="w")


           if data['current'] >= data['goal']:
               action_text = "Status: Target secure. Maintain current track."
               lbl_color = "#2E7D32"
           else:
               action_text = f"Action Required: You must attend {data['days_needed']} more consecutive sessions to reach threshold."
               lbl_color = "#C62828"


           Label(card, text=action_text, font=("Arial", 10, "italic"), bg="white", fg=lbl_color).pack(anchor="w",
                                                                                                      pady=(4, 0))


       Button(self.analytics_frame, text="RETURN TO MENU", font=("Lilita One", 12), bg="#FFC107",
              command=self.go_home).pack(side="bottom", pady=30)


   def go_home(self):
       self.analytics_frame.pack_forget()
       HomePage(self.parent)




class FaqPage:
   def __init__(self, parent):
       self.parent = parent
       background_color = "#1D61BB"


       self.faq_frame = Frame(parent, bg=background_color)
       self.faq_frame.pack(fill="both", expand=True)


       self.center_wrapper = Frame(self.faq_frame, bg=background_color)
       self.center_wrapper.pack(expand=True)


       Label(self.center_wrapper, text="FREQUENTLY ASKED QUESTIONS", font=("Lilita One", 22), bg=background_color,
             fg="white").pack(pady=15)


       faqs = [
           ("How is the minimum percentage calculated?",
            "It divides days attended by total academic track terms multiplied by 100."),
           ("What if my absence has an official medical clearance?",
            "Provide documentation directly to the administration to update your file codes."),
           ("How often should I use the Predictive Analysis tool?",
            "Checking every week helps track trends before percentages drop too low.")
       ]


       for q, a in faqs:
           box = Frame(self.center_wrapper, bg="#2E66B6", padx=10, pady=8, bd=1, relief="groove")
           box.pack(fill="x", pady=6)
           Label(box, text=f"Q: {q}", font=("Arial", 11, "bold"), bg="#2E66B6", fg="#FFC107", anchor="w").pack(
               fill="x")
           Label(box, text=a, font=("Arial", 10), bg="#2E66B6", fg="white", wraplength=500, justify="left",
                 anchor="w").pack(fill="x", pady=(2, 0))


       Button(self.faq_frame, text="BACK TO HUB", font=("Lilita One", 12), bg="#E0E0E0", command=self.go_back).pack(
           side="bottom", pady=25)


   def go_back(self):
       self.faq_frame.pack_forget()
       HomePage(self.parent)




class FactsPage:
   def __init__(self, parent):
       self.parent = parent
       background_color = "#1D61BB"


       self.facts_frame = Frame(parent, bg=background_color)
       self.facts_frame.pack(fill="both", expand=True)


       self.center_wrapper = Frame(self.facts_frame, bg=background_color)
       self.center_wrapper.pack(expand=True)


       Label(self.center_wrapper, text="ATTENDANCE RESEARCH INSIGHTS", font=("Lilita One", 22), bg=background_color,
             fg="white").pack(pady=20)


       # Dynamic text container block mapping layout 9.png
       self.fact_display = Message(self.center_wrapper, text="Click 'GENERATE' to load an attendance fact module.",
                                   font=("Arial", 13, "italic"), bg="#FFFFFF", fg="#333333", width=450, padx=20,
                                   pady=20, relief="sunken", bd=1)
       self.fact_display.pack(pady=15)


       self.gen_btn = Button(self.center_wrapper, text="GENERATE NEW FACT", font=("Lilita One", 13), bg="#FFC107",
                             fg="black", padx=10, pady=5, command=self.cycle_facts)
       self.gen_btn.pack(pady=10)


       Button(self.facts_frame, text="BACK TO HUB", font=("Lilita One", 12), bg="#E0E0E0", command=self.go_back).pack(
           side="bottom", pady=35)


   def cycle_facts(self):
       current_fact = random.choice(ATTENDANCE_FACTS)
       self.fact_display.config(text=current_fact)


   def go_back(self):
       self.facts_frame.pack_forget()
       HomePage(self.parent)




if __name__ == "__main__":
   root = Tk()
   root.resizable(False, False)  # Keeps layouts locked to your specific image frame sizes
   app = LoginPage(root)
   root.mainloop()









