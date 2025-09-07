import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def stream_users_in_batches(batch_size):
    """Stream users from DB in batches."""
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


def batch_processing(batch_size):
    """Process users in batches and print only those with age > 25."""
    for user_batch in stream_users_in_batches(batch_size):
        for user in user_batch:
            if user and user["age"] > 25:
                print(user)
    return


if __name__ == "__main__":
    # Example run with batch size of 5
    batch_processing(5)
