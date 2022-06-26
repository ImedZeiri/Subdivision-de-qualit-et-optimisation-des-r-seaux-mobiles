import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3

from PIL import ImageTk

from BackEnd.Services.Auth.Login import Login_Service
from BackEnd.Routers.Role import UserRole
from BackEnd.Services.Talk import Talk

class Login:
    def mainLogin():
        Window = Tk()
        Window.title("Login")
        Window.geometry("1141x628")
        Window.minsize(1141, 628)
        Window.maxsize(1141, 628)
        bg = ImageTk.PhotoImage(file="../Assets/BackGround.png")
        canvas = Canvas(Window, width=700, height=3500)
        canvas.pack(fill=BOTH, expand=True)
        canvas.create_image(0, 0, image=bg, anchor='nw')

        def resize_image(e):
            global image, resized, image2
            image = Image.open("../Assets/BackGround.png")
            resized = image.resize((e.width, e.height), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(resized)
            canvas.create_image(0, 0, image=image2, anchor='nw')
        Window.bind("<Configure>", resize_image)

        EntryEmail = Entry(Window)
        EntryEmail.place(relx=0.162, rely=0.464, height=30, relwidth=0.221)
        EntryEmail.configure(background="white")
        EntryEmail.configure(disabledforeground="white", bd=0)
        EntryEmail.configure(font="TkFixedFont")
        EntryEmail.configure(highlightbackground = "white", highlightcolor= "white")
        EntryEmail.configure(insertbackground="black")
        EntryEmail.insert(0, 'Email')

        EntryPassword = Entry(Window)
        EntryPassword.place(relx=0.162, rely=0.584, height=30, relwidth=0.221)
        EntryPassword.configure(background="white")
        EntryPassword.configure(disabledforeground="white", bd=0)
        EntryPassword.configure(font="TkFixedFont")
        EntryPassword.configure(highlightbackground = "white", highlightcolor= "white")
        EntryPassword.configure(insertbackground="black", show="*")
        EntryPassword.insert(0, 'Password')

        def destroy():
            time.sleep(1)
            Window.destroy()

        def Se_connecter():
            try:
                Email = EntryEmail.get()
                Password = EntryPassword.get()
                resultat = [Email,Password]
                Role = Login_Service.Specification_Role(resultat)
                destroy()
                TextToTalk = ("welcome  "+Role)
                say = Talk.Talk(TextToTalk)
                say
                RunWindowUser = UserRole.Routage(Role)
                RunWindowUser
            except:
                return False
        LgImg = PhotoImage(file="../Assets/BTN/BouttonConnexion.png")
        bConnexin = Button(Window)
        bConnexin.place(relx=0.3, rely=0.690, height=40, width=144)
        bConnexin.configure(activebackground="#ececec")
        bConnexin.configure(activeforeground="#000000")
        bConnexin.configure(background="#d9d9d9")
        bConnexin.configure(disabledforeground="#a3a3a3")
        bConnexin.configure(foreground="#000000")
        bConnexin.configure(highlightbackground="#d9d9d9")
        bConnexin.configure(highlightcolor="black")
        bConnexin.configure(pady="0", bd=0)
        bConnexin.configure(image=LgImg)
        bConnexin.configure(command=Se_connecter)

        Window.mainloop()
    mainLogin()
