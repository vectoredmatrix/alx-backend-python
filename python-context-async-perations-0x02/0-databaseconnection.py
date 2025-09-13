class ExecuteQuery:
    
    def __init__(self , db):
        
        self.db = db
        pass
    def __enter__(self):
        import sqlite3
        self.conn = sqlite3.connect(self.db)
        cursor = self.conn.cursor()
        return cursor
        
    def __exit__(self , exc_type , exc_val, traceback):
        self.conn.close()
    
    

#s = ExecuteQuery("m")

with ExecuteQuery("testdb.sqlite3") as cursor:
    r =  cursor.execute("SELECT * FROM users WHERE age > ?" , (25,))
    print(r.fetchall())