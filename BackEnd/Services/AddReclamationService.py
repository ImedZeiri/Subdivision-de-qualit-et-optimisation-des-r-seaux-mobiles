import sqlite3

from BackEnd.DB_Intializer.Db import Db_Connexion

class AddReclamationService:
    def Add_Rec(Sub,Content):
        t=Db_Connexion.Create_DataBase(self=True)
        t
        print("table created")
        conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
        l = conn.cursor()
        l.execute(
            "INSERT INTO Reclamation VALUES(:Sub, :Content)",
            {
             'Sub': Sub,
             'Content':Content
             })
        conn.commit()
        conn.close()