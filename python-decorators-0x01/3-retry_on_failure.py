import sqlite3 , time



def with_db_connection(func):
    def wrapper (*args , **kwargs):
       
        conn = sqlite3.connect("testdb.sqlite3")
        try:
            result = func(conn , *args , **kwargs)
        finally:
            conn.close()
        return result
    
    return wrapper


def retry_on_failure(retries , delay):
    def dec(func):
        def wrapper(conn , *args , **kwargs):
            attempt =0
            while attempt < retries:
                try :
                    return func(conn ,*args, **kwargs)
                
                except Exception as e:
                    attempt += 1
                    print(attempt)
                    print("failed {} attempt .... retrying".format(attempt))
                  
                    if attempt == retries:
                        print(e)
                        raise
                    time.sleep(delay)
    
        return wrapper
    return dec

@with_db_connection
@retry_on_failure(retries=3 , delay =1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM Users ;")
    return result.fetchall()


users = fetch_users_with_retry()

print(users)