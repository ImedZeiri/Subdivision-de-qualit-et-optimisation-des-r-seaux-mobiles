import sqlite3

DataTest = ["EmailTest","FirstTest","LastTest","PassTest","RoleTest"]
conn = sqlite3.connect('/Users/macbookpro/Desktop/PFE_MOUNA/BackEnd/DB_Intializer/DataBase.db')
l = conn.cursor()
l.execute(
    "INSERT INTO User values(NULL,'Manager','Manager','Manager','Manager','Manager','Manager')")
conn.commit()
conn.close()