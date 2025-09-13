import time , sqlite3 , functools

query_cache =  {}


def with_db_connection(func):
    def wrapper(*args , **kwargs):
        conn = sqlite3.connect("testdb.sqlite3")
        try:
            
            result =  func(conn , *args, **kwargs)
        
        finally:
            conn.close()
            
        return result
    return wrapper


def cache_query(func):
    def wrapper(conn ,*args, **kwargs ):
        
        print(kwargs["query"])
        print(len(list(query_cache.keys())))
        total_key = list(query_cache.keys())
        #for v in query_cache.values():
        if kwargs["query"] in query_cache.values():
            pass #continue
        else :
            query_cache[len(total_key) + 1] = kwargs['query']
        
        return func(conn , *args , **kwargs)
    
    return wrapper
                
                


@with_db_connection
@cache_query
def fetch_users_with_cache(conn , query) :
    cursor = conn.cursor()
    cursor.execute(query)
    
    return cursor.fetchall()


users = fetch_users_with_cache(query="SELECT * FROM Users ;")
        
print(users)
    
       