import mysql.connector

def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="FastAPI123!",
        database="students"
    )

def injection():
    conn = connection()
    try:
        yield conn
    finally:
        conn.close()