import sqlite3
from BackEnd.DB_Intializer.Db import Db_Connexion

def Try_Connexion():
    try:
        conn = sqlite3.connect('DataBase.db')
        c = conn.cursor()
        Db_Connexion.Create_DataBase(self=True)
        print("Data Base Connected succefully !!")
        c.close()

        return True
    except:
        return False

Try_Connexion()
