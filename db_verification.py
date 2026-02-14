from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

app=FastAPI()

def connection():
    info=mysql.connector.connect(
        host="localhost",
        user="root",
        password="FastAPI123!",
        database="students"
    )

    return info

@app.get("/")
def entry():
    return f"Verification Page"


@app.get("/verify")
def verify():
    try:
        con=connection()
        cursor=con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student_info")
        data=cursor.fetchall()
        cursor.close()
        con.close()
        return data

    except Error as e:
        return f"{e}"
