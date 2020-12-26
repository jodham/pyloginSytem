from tkinter import *

class MainWindow:
    def __init__(self):
        self.app = Tk()
        self.app.title("python login")
        self.app.geometry("300x250")
        self.label1 = Label(self.app, text="Welcome to app")
        self.label1.place(x=95, y=40)
        self.login = Button(self.app, text="Login", pady=5, padx=30,command=login)
        self.login.place(x=100, y=80)
        self.login = Button(self.app, text="Register", pady=5, padx=30,command= register)
        self.login.place(x=100, y=120)

    def run(self):
         self.app.mainloop()

    def Login(self):
        loginTk = Login()
        loginTk.run()

    def Register(self):
        registerTk = Register()
        registerTk.run



app = MainWindow()
app.run()
