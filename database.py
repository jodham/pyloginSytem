import _sqlite3
import bcrypt

class Database:
    def __init__(self):
        try:
            self.conn = _sqlite3.connect("test.db")
            print("successfully opened database")
            self.curr = self.conn.cursor()
        except:
            print("Failed")
def createTable(self):
 create_table='''CREATE TABLE IF NOT EXISTS cred(
        id Integer PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL);'''
 self.curr.execute(create_table)
 self.conn.commit()

 def insertData(self,data):
     

