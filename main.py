from tkinter import *
from PIL import Image, ImageTk # imports modules for image resizing and display

name_list = [] # stores all the entered names
user_name = "" # stores the user's current name


class LoginPage:
    def __init__(self, parent):
        background_color = "#1D61BB"  # sets the background colour

        self.image = Image.open("Attendance Analytics.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.img_width, self.img_height = self.image.size
        parent.geometry(f"{self.img_width}x{self.img_height}")
        parent.title("Attendance Analytics")

        self.login_frame = Frame(parent, bg=background_color)
        self.login_frame.pack(fill="both", expand=True)

        self.bg_label = Label(self.login_frame, image=self.photo, bd=0)
        self.bg_label.place(x=0, y=0)  # only exception (background ONLY)

        self.bg_label = Label(self.login_frame, image=self.photo, bd=0)
        self.bg_label.place(x=0, y=0)  # only exception (background ONLY)

        self.container = Frame(self.login_frame, bg=background_color)
        self.container.pack(expand=True)

        self.text_canvas = Canvas(self.container, width=400, height=120, bg=background_color, highlightthickness=0)
        self.text_canvas.pack(pady=0, padx=(0,100))

        self.text_canvas.create_text(202, 90, text="NAME", font=("Lilita One", 36), fill="black")
        self.text_canvas.create_text(200, 88, text="NAME", font=("Lilita One", 36), fill="white")

        self.entry_box = Entry(self.container, width=22, font=("Lilita One", 16))
        self.entry_box.pack(pady=22, padx=(0, 100))

        self.continue_button = Button(self.container, text="ENTER", font=("Lilita One", 14), state="disabled", command=self.name_collect)
        self.continue_button.pack(pady=0, padx=(0, 100))

        self.error_label = Label(self.container, text="", fg="red", bg=background_color, font=("Lilita One", 11))
        self.error_label.pack(pady=0, padx=(0, 100))

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

    # stores the users name and initiates the quiz
    def name_collect(self):
        global user_name
        name = self.entry_box.get().strip()
        if name:
            user_name = name
            name_list.append(name)
            print("Current User:", user_name)
            print("All Names:", name_list)

class homepage:
    def __init__(self, parent):
        background_color = "#D8CAB8"  # sets background colour
        # sets up frame

        self.image = Image.open("Attendance Analytics.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.img_width, self.img_height = self.image.size
        parent.geometry(f"{self.img_width}x{self.img_height}")
        parent.title("Attendance Analytics")

        self.home_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        self.home_frame.grid()

        if __name__ == "__main__":


            root = Tk()
            LoginPage(root)
            root.mainloop()









