import mysql.connector

"""Defining MySql connection for the database root which is the main database"""
def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="FastAPI123!",
        database="students"
    )

"""A reusable function for starting connection and then terminating it after work"""
def injection():
    conn = connection()
    try:
        yield conn
    finally:
        conn.close()