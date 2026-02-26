from db_verification import connection
from fastapi import Depends

def injection():
    conn=connection()
    try:
        yield conn
    finally:
        conn.close()