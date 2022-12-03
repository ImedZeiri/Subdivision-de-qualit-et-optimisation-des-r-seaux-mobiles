import sqlite3
from BackEnd.DB_Intializer.Db import Db_Connexion
import BackEnd.DB_Intializer.Connexion


DataTest = ["EmailTest","FirstTest","LastTest","PassTest","RoleTest"]



class Add:
    def Add_Test(DataTest):
        t=Db_Connexion.Create_DataBase(self=True)
        t
        print("table created")
        conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
        l = conn.cursor()
        l.execute(
            "INSERT INTO Test VALUES(:Email, :FirstName, :LastName, :Password, :Role)",
            {'Email': DataTest[0],
             'FirstName': DataTest[1],
             'LastName': DataTest[2],
             'Password': DataTest[3],
             'Role': DataTest[4]
             })
        conn.commit()
        conn.close()

    def Add_Ing(DataIngineer):
        t=Db_Connexion.Create_DataBase(self=True)
        t
        print("table created")
        conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
        l = conn.cursor()
        l.execute(
            "INSERT INTO user VALUES(:Email, :FirstName, :LastName, :Password, :Role)",
            {'Email': DataIngineer[0],
             'FirstName': DataIngineer[1],
             'LastName': DataIngineer[2],
             'Password': DataIngineer[3],
             'Role': DataIngineer[4]
             })
        conn.commit()
        conn.close()

    def Add_Tech(DataTech):
        t=Db_Connexion.Create_DataBase(self=True)
        t
        print("table created")
        conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
        l = conn.cursor()
        l.execute(
            "INSERT INTO user VALUES(:Email, :FirstName, :LastName, :Password, :Role)",
            {'Email': DataTech[0],
             'FirstName': DataTech[1],
             'LastName': DataTech[2],
             'Password': DataTech[3],
             'Role': DataTech[4]
             })
        conn.commit()
        conn.close()

    def Add_SrClt(DataSC):
        t=Db_Connexion.Create_DataBase(self=True)
        t
        print("table created")
        conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
        l = conn.cursor()
        l.execute(
            "INSERT INTO user VALUES(:Email, :FirstName, :LastName, :Password, :Role)",
            {'Email': DataSC[0],
             'FirstName': DataSC[1],
             'LastName': DataSC[2],
             'Password': DataSC[3],
             'Role': DataSC[4]
             })
        conn.commit()
        conn.close()

    def Add_Admin(DataAdmin):
        t=Db_Connexion.Create_DataBase(self=True)
        t
        print("table created")
        conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
        l = conn.cursor()
        l.execute(
            "INSERT INTO user VALUES(:Email, :FirstName, :LastName, :Password, :Role)",
            {'Email': DataAdmin[0],
             'FirstName': DataAdmin[1],
             'LastName': DataAdmin[2],
             'Password': DataAdmin[3],
             'Role': DataAdmin[4]
             })
        conn.commit()
        conn.close()

