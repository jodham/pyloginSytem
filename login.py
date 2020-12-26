from tkinter import *
from tkinter import messagebox
import bcrypt
from database import Database

db = Database()
db.createTable()

class Login:
    def __init__(self):
        self.loginWindow = Tk()
        self.loginWindow.title("Login")
        self.loginWindow.geometry("300x250")
        self.label = Label(self.loginWindow, text="login")
        self.label.place(x=95, y=40)

        self.usernameS = StringVar()
        self.passwordS = StringVar()

        self.usernameE = Entry(self.loginWindow, relief =FLAT, textvariable=self.usernameS)
        self.usernameE.place(x=100, y=120)
        self.passwordE = Entry(self.loginWindow, show="*"
                               ,relief=FLAT,textvariable=self.passwordS)
        self.passwordE.place(x=100, y=150)

        self.username = self.usernameS.get()
        self.password = self.passwordE.get()

        self.submit = Button(self.loginWindow, text="submit", pady=5, padx=20
                             , command=self.validate)
        self.submit.place(x=100, y=150)