import sqlite3
import random

from BackEnd.DB_Intializer.Db import Db_Connexion

class AddReclamationService:
    def Add_Rec(Sub,Content,State):
        id = random.randint(1, 10)
        t=Db_Connexion.Create_DataBase(self=True)
        t
        print("table created")
        conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
        l = conn.cursor()
        l.execute(
            "INSERT INTO reclamations VALUES(:Sub, :Content, :State, :id)",
            {
                'id':id,
                'utilisateur': Sub,
                'description':Content,
                'statut':State
             })
        conn.commit()
        conn.close()
