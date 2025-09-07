import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def stream_users(batch_size=10):
    """Stream rows from user_data in batches."""
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        database=os.getenv("DB_NAME", "ALX_prodev"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD")
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

    cursor.close()
    connection.close()


def batch_processing(batch_size=10):
    """Process users in batches."""
    for user_batch in stream_users(batch_size):
        for user in user_batch:
            # Ensure age is an integer
            age = int(user["age"]) if user["age"] is not None else 0
            if age > 25:
                print(user)


if __name__ == "__main__":
    print("📌 All users in database:")
    for user_batch in stream_users(batch_size=5):  # change batch size here
        for user in user_batch:
            print(user)

    print(" Users older than 25:")
    batch_processing(batch_size=5)
