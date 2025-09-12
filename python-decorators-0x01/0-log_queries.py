import sqlite3 , functools
from datetime import datetime


def log_queries(func):
    def wrapper(*args , **kwargs):
        print(*args)
        result = func (*args , **kwargs)
        
        return result

    return wrapper
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect("testdb.sqlite3")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


user = fetch_all_users("SELECT * FROM Users WHERE age < 10")
print(user)