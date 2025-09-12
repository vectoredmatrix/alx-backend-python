import sqlite3 , functools


def log_queries(func):
    def wrapper(*args , **kwargs):
        pass

    return wrapper

def fetch_all_users(query):
    conn = sqlite3.connect("testdb.sqlite3")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


user = fetch_all_users("SELECT * FROM Users WHERE age < 10")
print(user)