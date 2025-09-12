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



def transactional(func):
    def wrapper(conn, *args, **kwargs):
       try:
           result =func (conn ,*args, **kwargs)
           conn.commit()
           print("excuted")
           return result
        
       except:
           conn.rollback()
           
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn , user_id , new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE Users SET email = ? WHERE id = ?" , (new_email , user_id))
    
    
    

update_user_email(user_id=1 , new_email="Lawalsulaimon987@gmail.com")