import sqlite3
from BackEnd.Entity.AdminInterface import AdminInterface

class Db_Connexion:
    def Create_DataBase(self):
        #Admin =AdminInterface ("mouna1@gmail.com","mouna","chmengui","admin")
        #Admin.TestAdminExisted()
        #print(Admin.id)
        conn = sqlite3.connect('../DB_Intializer/DataBase.db')
        c = conn.cursor()
        #creation de tous les classes
        c.execute("CREATE TABLE IF NOT EXISTS User (Email TEXT,FirstName TEXT,LastName TEXT, Password TEXT,Role TEXT )")
        c.execute("CREATE TABLE IF NOT EXISTS Test (Email TEXT,FirstName TEXT,LastName TEXT, Password TEXT,Role TEXT )")
        c.execute("CREATE TABLE IF NOT EXISTS DirectionRegionale (ID int,tel TEXT,nom TEXT, localisation TEXT,tache TEXT )")

        print("Data Base Created succefully !!")
        #todo
        #implementation de tout les classes



if __name__ == '__main__':
    Db_Connexion.Create_DataBase(self=True)
