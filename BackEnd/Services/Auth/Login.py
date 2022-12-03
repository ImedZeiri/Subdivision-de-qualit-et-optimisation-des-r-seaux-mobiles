import time
from tkinter import *
from tkinter import messagebox
import sqlite3

class Login_Service:
    def Specification_Role(resultat):
        try:
            res = resultat
            Email_Entry = str(res[0])
            Password_Entry = str(res[1])
            conn = sqlite3.connect('/Users/macbookpro/desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
            c = conn.cursor()
            c.execute(
                " select distinct Role from User where mail ='" + Email_Entry + "' and password ='" + Password_Entry + "';")
            NextScreen = c.fetchone()
            Role = NextScreen[0]
            c.close()
            print(type(Role))
            print(Role)
            return Role
        except:
            messagebox.showwarning("","No user data with this info")
    Role = Specification_Role



    def login_verify():
        global username1
        global password1
        username1 = Entry1.get()
        password1 = Entry2.get()

        print('email')
        print(username1)
        print('password')
        print(password1)
        Entry1.delete(0, END)
        Entry2.delete(0, END)

        ###############################################################

        try:
            conn = sqlite3.connect('../BD/data.db')
            cur = conn.cursor()
            cur.execute(
                " select distinct v6 from Utilisateur where v7 ='" + username1 + "' and v4 ='" + password1 + "';")
            role = cur.fetchone()
            conn.commit()
            conn.close()
            global verif
            verif = role[0]
            print("-----------------------")
            print(role)
            print("-----------------------")
            print(role[0])

            l = ['admin', 'tech', 'cont']
            if role[0] in l:
                if role[0] == l[0]:
                    login_sucess(1)
                if role[0] == l[1]:
                    login_sucess(2)
                if role[0] == l[2]:
                    login_sucess(3)


        except:
            if role == None:
                messagebox.showwarning("", "Verifier Votre Saisie")
