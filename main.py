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

       self.heading_label.create_text(self.login_frame, text="Welcome to the login page", font=("Lilita One", 64), fill="white")


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
       self.exit_button.place(x=1800, y=530)


       self.back_button = Button(self.home_frame, text="BACK", font=("Lilita One", 12), bg="#D32F2F", fg="white", bd=0,
                                 padx=15, pady=5, command=self.parent.quit)
       self.back_button.place(x=15, y=530)


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

        self.frame = Frame(parent, bg="#1D61BB")
        self.frame.pack(fill="both", expand=True)

        Label(
            self.frame,
            text="CALCULATOR PAGE",
            font=("Lilita One", 28),
            bg="#1D61BB",
            fg="white"
        ).pack(pady=(10, 0))

        Label(
            self.frame,
            text="CALCULATE YOUR ATTENDANCE(S) BELOW",
            font="Lilita One",
            bg="#1D61BB",
            fg="white"
        ).pack(pady=(10, 10))

        self.subject_count = 1

        self.table_frame = Frame(
            self.frame,
            bg="#E7B96D",
            highlightbackground="black",
            highlightthickness=4
        )
        self.table_frame.pack(pady=10)

        headers = [
            "SUBJECTS",
            "DAYS ATTENDED",
            "TOTAL DAYS",
            "MIN. ATTENDANCE",
            "ATTENDANCE"
        ]

        widths = [20, 20, 18, 22, 20]

        for col, header in enumerate(headers):
            Label(
                self.table_frame,
                text=header,
                font="Lilita One",
                bg="#E7B96D"
            ).grid(row=0, column=col, padx=0, pady=10)

        self.subject_entries = []

        self.add_row()

        Button(
            self.frame,
            text="CHECK ANALYTICS",
            font="Lilita One",
            bg="#7ED957",
            command=self.open_analytics
        ).pack(pady=15)

        Label(
            self.frame,
            text="NO. OF SUBJECTS",
            font="Lilita One",
            bg="#1D61BB",
            fg="white"
        ).pack()

        counter_frame = Frame(self.frame, bg="#1D61BB")
        counter_frame.pack()

        Button(
            counter_frame,
            text="-",
            font=("Lilita One", 20, "bold"),
            width=2,
            command=self.remove_row
        ).pack(side="left", padx=10)

        self.counter_lbl = Label(
            counter_frame,
            text=str(self.subject_count),
            font="Lilita One",
            bg="#E7B96D",
            width=3
        )
        self.counter_lbl.pack(side="left")

        Button(
            counter_frame,
            text="+",
            font=("Lilita One", 20, "bold"),
            width=2,
            command=self.add_row
        ).pack(side="left", padx=10)

        add_nav_buttons(
            self.frame,
            lambda: self.go_back(),
            parent.quit
        )

    def add_row(self):
        row_num = len(self.subject_entries) + 1

        subject = Entry(self.table_frame, width=18)
        attended = Entry(self.table_frame, width=15)
        total = Entry(self.table_frame, width=15)

        min_attendance = Label(
            self.table_frame,
            text="90%",
            bg="#E7B96D",
            font="Lilita One"
        )

        attendance = Label(
            self.table_frame,
            text="-",
            bg="#E7B96D",
            font="Lilita One"
        )

        subject.grid(row=row_num, column=0, padx=5, pady=5)
        attended.grid(row=row_num, column=1, padx=5, pady=5)
        total.grid(row=row_num, column=2, padx=5, pady=5)
        min_attendance.grid(row=row_num, column=3, padx=5, pady=5)
        attendance.grid(row=row_num, column=4, padx=5, pady=5)

        self.subject_entries.append(
            (subject, attended, total, attendance)
        )

        self.subject_count = len(self.subject_entries)
        self.counter_lbl.config(text=str(self.subject_count))

    def remove_row(self):
        if len(self.subject_entries) > 1:
            row = self.subject_entries.pop()

            for widget in row:
                widget.destroy()

            self.subject_count = len(self.subject_entries)
            self.counter_lbl.config(text=str(self.subject_count))

    def open_analytics(self):
        self.frame.pack_forget()
        AnalyticsPage(self.parent)

    def go_back(self):
        self.frame.pack_forget()
        HomePage(self.parent)


class AnalyticsPage:
    def __init__(self, parent):
        self.parent = parent

        self.frame = Frame(parent, bg="#1D61BB")
        self.frame.pack(fill="both", expand=True)

        Label(
            self.frame,
            text="ANALYTICS PAGE",
            font=("Lilita One", 28),
            bg="#1D61BB",
            fg="white"
        ).pack(pady=(10, 0))

        Label(
            self.frame,
            text="THIS DISPLAYS AN ANALYSIS OF YOUR ATTENDANCE",
            font="Lilita One",
            bg="#1D61BB",
            fg="white"
        ).pack(pady=(10, 10))

        table_frame = Frame(
            self.frame,
            bg="#E7B96D",
            highlightbackground="black",
            highlightthickness=4
        )
        table_frame.pack(pady=20)

        headers = [
            "SUBJECTS",
            "DAYS TO REACH THRESHOLD",
            "% CHANGE FROM LAST CALCULATION"
        ]

        for col, header in enumerate(headers):
            Label(
                table_frame,
                text=header,
                font="Lilita One",
                bg="#E7B96D"
            ).grid(row=0, column=col, padx=20, pady=10)

        for i in range(8):
            Entry(table_frame, width=20).grid(row=i + 1, column=0, padx=10, pady=5)
            Entry(table_frame, width=30).grid(row=i + 1, column=1, padx=10, pady=5)
            Entry(table_frame, width=30).grid(row=i + 1, column=2, padx=10, pady=5)

        add_nav_buttons(
            self.frame,
            lambda: self.go_back(),
            parent.quit
        )

    def go_back(self):
        self.frame.pack_forget()
        CalculatorPage(self.parent)





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
           ("How is the attendance percentage calculated?",
            "It divides days attended by total academic track terms multiplied by 100."),
           ("How do I avoid lateness/truances?",
            "try consistently leaving early to have more than enough time to arrive."),
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









