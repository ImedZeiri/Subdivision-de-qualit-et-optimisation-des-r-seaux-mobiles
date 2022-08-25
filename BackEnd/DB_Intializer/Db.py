import sqlite3
from BackEnd.Entity.AdminInterface import AdminInterface

class Db_Connexion:
    def Create_DataBase(self):
        conn = sqlite3.connect("DataBase.db")
        c = conn.cursor()
        #creation de tous les classes
        c.execute("CREATE TABLE IF NOT EXISTS User (pid INTEGER PRIMARY KEY,"
                  "name TEXT NOT NULL,"
                  "age TEXT NOT NULL,"
                  "gender TEXT NOT NULL,"
                  "mail TEXT NOT NULL,"
                  "Role TEXT NOT NULL,"
                  "password TEXT NOT NULL  "
                  ")")
        c.execute("CREATE TABLE IF NOT EXISTS DirectionRegionale (ID int,tel TEXT,nom TEXT, localisation TEXT,tache TEXT )")

        print("Data Base Created succefully !!")
        #todo
        #implementation de tout les classes



if __name__ == '__main__':
    Db_Connexion.Create_DataBase(self=True)
