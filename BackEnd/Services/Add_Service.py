import sqlite3
from BackEnd.DB_Intializer.Db import Db_Connexion

DataTest = ["EmailTest","FirstTest","LastTest","PassTest","RoleTest"]

class Add:
    def Add_Test(DataTest):
        t=Db_Connexion.Create_DataBase(self=True)
        t
        print("table created")
        conn = sqlite3.connect('../DB_Intializer/DataBase.db')
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
    Add_Test(DataTest)
    #todo
    #add user
    #add de tous les classes ou bien les entiers
