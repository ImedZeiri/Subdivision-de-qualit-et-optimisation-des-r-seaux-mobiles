import sqlite3


class Read_Service:
    def ReadAdminData():
        conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
        l = conn.cursor()
        Data = l.execute("SELECT DISTINCT * FROM User where (Role Like 'Manager')")
        conn.commit()
        rows= Data.fetchall()
        return rows

    def ReadIngData():
        conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
        l = conn.cursor()
        Data = l.execute("SELECT DISTINCT * FROM User where (Role Like 'Ingineer')")
        conn.commit()
        rows= Data.fetchall()
        return rows

    def ReadTechData():
        conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
        l = conn.cursor()
        Data = l.execute("SELECT DISTINCT * FROM User where (Role Like 'Technicien')")
        conn.commit()
        rows= Data.fetchall()
        return rows

    def ReadScData():
        conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
        l = conn.cursor()
        Data = l.execute("SELECT DISTINCT * FROM User where (Role Like 'ServiceClient')")
        conn.commit()
        rows= Data.fetchall()
        return rows





