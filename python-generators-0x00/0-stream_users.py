import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def stream_users():
    """Stream all rows from user_data one by one (no parameters allowed)."""
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        database=os.getenv("DB_NAME", "ALX_prodev"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD")
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:   # yield rows one at a time
        yield row

    cursor.close()
    connection.close()


if __name__ == "__main__":
    print("📌 Streaming users row by row:")
    for user in stream_users():
        print(user)
