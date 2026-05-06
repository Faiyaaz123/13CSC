from tkinter import *
from PIL import Image, ImageTk # imports modules for image resizing and display

name_list = [] # stores all the entered names
user_name = "" # stores the user's current name


class LoginPage:
 def __init__(self, parent):
     self.LoginPage = None
     background_color = "#1D61BB"  # sets the background colour
     self.login_frame = Frame(parent, bg=background_color, padx=100, pady=100)
     self.login_frame.grid()
     image = Image.open("Screenshot 2026-04-28 115831.png")
     image = image.resize((250, 125))
     self.photo = ImageTk.PhotoImage("Screenshot 2026-04-28 115831.png")
     self.image_label = Label(self.LoginPage, image=self.photo, bg=background_color)
     self.image_label.grid(row=0, column=0, pady=(1, 50))
     # entry box for the user to input their username
     self.entry_box = Entry(self.LoginPage, width=20, font=("Verdana", 16),)
     self.entry_box.grid(row=3, column=0, pady=20, )
     self.entry_box.bind("<KeyRelease>", self.validate_name)
     # label to display the error message for if the user types out an invalid name
     self.error_label = Label(self.LoginPage, text="", fg="red", bg=background_color, font=("Verdana", 11))
     self.error_label.grid(row=4, column=0)
     # button to enter the user's name so they can move onto the quiz section and is initially disabled
     self.continue_button = Button(self.LoginPage, text="Enter",
                                   font=("Lilita One", 12, "bold"), bg="yellow",
                                   command=self.name_collect, width=12)
     self.continue_button.grid(row=5, column=0, pady=20)
     self.continue_button.config(state="disabled")
 # Validates users name
 def validate_name(self, event=None):
     name = self.entry_box.get().strip()
     if len(name) < 2:  #conditional statement for if the user's typed out name is less than 2 letters
         self.error_label.config(text="⚠ Name must be at least 2 letters.")
         self.continue_button.config(state="disabled")
     elif not name.isalpha():  #conditional statement for if the user's typed out name does not only contain letters
         self.error_label.config(text="⚠ Name must contain only letters.")
         self.continue_button.config(state="disabled")
     else: # conditional statement for if the 2 above conditional statements are not met which leads to the enter button being enabled
         self.error_label.config(text="")
         self.continue_button.config(state="normal")

 # stores the users name and initiates the quiz
 def name_collect(self):
     global user_name
     name = self.entry_box.get().strip()
     if name:
         user_name = name
         name_list.append(name)
         self.login_frame.destroy()

 if __name__ == "__main__":
     root = Tk()  # creates the central Tkinter window
     root.title("Attendance Analytics")  # name of the window
     LoginPage: root  # shows the starting screen of the programme(username entry)
     root.mainloop()  # keeps window open







