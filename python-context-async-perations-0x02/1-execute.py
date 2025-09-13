class ExecuteQuery:
    
    def __init__(self , db , query , param = None):
        
        self.db = db
        self.query = query
        self.param = param or ()
        
    def __enter__(self):
        import sqlite3
        self.conn = sqlite3.connect(self.db)
        cursor = self.conn.cursor()
        result = cursor.execute(self.query , self.param)
        return result
        
    def __exit__(self , exc_type , exc_val, traceback):
        self.conn.close()
    
    

#s = ExecuteQuery("m")

with ExecuteQuery("testdb.sqlite3" , "SELECT * FROM users WHERE age > ?" , (25,))  as cursor:
    
    print(cursor.fetchall())