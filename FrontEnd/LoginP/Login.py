import time
from tkinter import *
from tkinter import ttk
import sqlite3
from BackEnd.Services.Auth.Login import Login_Service
from BackEnd.Routers.Role import UserRole

class Login:
    def mainLogin():
        Window = Tk()
        Window.title("Login")
        Window.geometry("1041x588")
        Window.maxsize(1041, 588)
        Window.minsize(1041, 588)
        Label1 = Label(Window)
        Label1.place(relx=0.05, rely=0.11, height=21, width=100)
        Label1.configure(background="white")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(foreground="#000000")
        Label1.configure(text='''Email :''', anchor=W)

        EntryEmail = Entry(Window)
        EntryEmail.place(relx=0.22, rely=0.11, height=20, relwidth=0.191)

        Label2 = Label(Window)
        Label2.place(relx=0.05, rely=0.198, height=21, width=100)
        Label2.configure(background="white")
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(foreground="#000000")
        Label2.configure(text='''Password :''', anchor=W)

        EntryPassword = Entry(Window)
        EntryPassword.place(relx=0.22, rely=0.286, height=20, relwidth=0.191)

        def destroy():
            time.sleep(1)
            Window.destroy()


        def Se_connecter():
            Email = EntryEmail.get()
            Password = EntryPassword.get()
            resultat = [Email,Password]
            a = Login_Service.Specification_Role(resultat)
            destroy()
            b = UserRole.Routage(a)
            b




        bConnexin = Button(Window)
        bConnexin.place(relx=0.593, rely=0.80, height=33, width=174)
        bConnexin.configure(activebackground="#ececec")
        bConnexin.configure(activeforeground="#000000")
        bConnexin.configure(background="#d9d9d9")
        bConnexin.configure(disabledforeground="#a3a3a3")
        bConnexin.configure(foreground="#000000")
        bConnexin.configure(highlightbackground="#d9d9d9")
        bConnexin.configure(highlightcolor="black")
        bConnexin.configure(pady="0", bd=0)
        bConnexin.configure(text="Se Connecter")
        bConnexin.configure(command=Se_connecter)

        Window.mainloop()
    mainLogin()
