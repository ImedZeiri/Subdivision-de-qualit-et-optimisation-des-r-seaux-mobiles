import sqlite3

class Db_Connexion:
    def Create_DataBase(self):
        conn = sqlite3.connect('DataBase.db')
        c = conn.cursor()
        #creation de tous les classes
        c.execute("CREATE TABLE IF NOT EXISTS User (Email TEXT,FirstName TEXT,LastName TEXT, Password TEXT,Role TEXT )")
        c.execute("CREATE TABLE IF NOT EXISTS Test (Email TEXT,FirstName TEXT,LastName TEXT, Password TEXT,Role TEXT )")
        c.close()
        print("Data Base Created succefully !!")



if __name__ == '__main__':
    Db_Connexion.Create_DataBase(self=True)
