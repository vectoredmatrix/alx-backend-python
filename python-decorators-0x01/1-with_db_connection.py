import sqlite3



def with_db_connection(func):
    def wrapper (*args , **kwargs):
        conn = sqlite3.connect("testdb.sqlite3")
        try:
            result = func(conn , *args , **kwargs)
        finally:
            conn.close()
        return result
        
    
    return wrapper


@with_db_connection
def get_user_by_id(conn , user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE id = ?" , (user_id,))
    return cursor.fetchone()



user = get_user_by_id(user_id = 1)
print(user)