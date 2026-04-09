import mysql.connector
import os

"""Defining MySql connection for the database root which is the main database"""
def connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "FastAPI123!"),
        database=os.environ.get("DB_NAME", "students"),
        port=int(os.environ.get("DB_PORT", 3306))
    )

"""A reusable function for starting connection and then terminating it after work"""
def injection():
    conn = connection()
    try:
        yield conn
    finally:
        conn.close()
