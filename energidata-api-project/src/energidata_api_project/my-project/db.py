import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")


try:
    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password
    )
    print("Connection succesful!")
    conn.close()
except Exception as e:
    print(f"Error: {e}")