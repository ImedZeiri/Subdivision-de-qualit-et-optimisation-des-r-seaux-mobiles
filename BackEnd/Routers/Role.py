import sqlite3
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from BackEnd.Services.Auth.Login import Login_Service

class UserRole:
    global userConnected,Email_Entry,Password_Entry
    def User_Identification(res):
        try:
            Role = Login_Service.Specification_Role(res)
            return Role
        except:
            Error = messagebox.showinfo("","There is now row with this data !! ")


    def Routage(Role):
        def Client():
            from FrontEnd.Client.Client_FE import Client
            Client.main()

        def Clien_service():
            from FrontEnd.Client_Service.Client_Service_FE import Client_Service
            Client_Service.main()

        def Ingineer():
            from FrontEnd.Ingineer.Ingineer_FE import Ingineer
            Ingineer.main()

        def Manager():
            from FrontEnd.Project_Manager.Manager_FE import Manager
            Manager.main_Manager()

        def Technicien():
            from FrontEnd.Technicien.Technicien_FE import Technicien
            Technicien.main()

        if Role == "Client":
            messagebox.showinfo("Welcome", "Bienvenue cher : " + Role)
            print("windw est destroy")
            time.sleep(1)
            print("1 s   est passee")
            Client()

        if Role == "Client_Service":
            messagebox.showinfo("Welcome", "Bienvenue cher : " + Role)
            print("windw est destroy")
            time.sleep(1)
            print("1 s   est passee")
            Clien_service()

        if Role == "Manager":
            messagebox.showinfo("Welcome", "Bienvenue cher : " + Role)
            print("windw est destroy")
            time.sleep(1)
            print("1 s   est passee")
            Manager()

        if Role == "Ingineer":
            messagebox.showinfo("Welcome", "Bienvenue cher : " + Role)
            print("windw est destroy")
            time.sleep(1)
            print("1 s   est passee")
            Ingineer()

        if Role == "Technicien":
            messagebox.showinfo("Welcome", "Bienvenue cher : " + Role)
            print("windw est destroy")
            time.sleep(1)
            print("1 s   est passee")
            Technicien()


    Role=User_Identification
    Routage(Role)
