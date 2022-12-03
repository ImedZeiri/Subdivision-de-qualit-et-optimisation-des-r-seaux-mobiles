import sqlite3

class IngineerService:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.c=self.con.cursor()
        self.c.execute("""
                        CREATE TABLE IF NOT EXISTS User(
                        pid INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        age TEXT NOT NULL,
                        gender TEXT NOT NULL,
                        mail TEXT NOT NULL,
                        Role TEXT NOT NULL,
                        password TEXT NOT NULL                    
                        )
                        """)
        self.con.commit()

    def insert(self,name,age,gender,mail,password):
        Role="Ingineer"
        sql="""
            insert into User values(NULL,?,?,?,?,?,?)
        """
        self.c.execute(sql,(name,age,gender,mail,Role,password))
        self.con.commit()

    def fetch_record(self):
        self.c.execute("SELECT DISTINCT * FROM User where (Role Like 'Ingineer')")
        data = self.c.fetchall()
        return data

    def update_record(self,name,age,gender,mail,password,pid):
        Role="Ingineer"
        sql="""
            update User set name=?,age=?,gender=?,mail=?,Role=?,password=? where pid=?
        """
        self.c.execute(sql,(name,age,gender,mail,Role,password,pid))
        self.con.commit()

    def remove_record(self,pid):
        sql="delete from User where pid=?"
        self.c.execute(sql,(pid,))
        self.con.commit()

