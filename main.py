from fastapi import FastAPI
from pydantic import BaseModel
from db_verification import connection
from typing import List
from typing import Optional

app=FastAPI()

class Student(BaseModel):
    id: Optional[int]=None
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    semester: Optional[int]=None

@app.post("/student")
def enter_data(entries: List[Student]):
    conn=connection()
    cursor=conn.cursor(dictionary=True)

    for entry in entries:

        query="INSERT INTO student_info (ID, First_Name, Last_Name, Semester) " \
            "VALUES (%s, %s, %s, %s)"
        values=(entry.id, entry.first_name, entry.last_name, entry.semester)
    
        cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return f"Table updated. Check database."

@app.get("/student/{student_id}")
def show_details(student_id:int):
    conn=connection()
    cursor=conn.cursor(dictionary=True)

    query="SELECT * FROM student_info WHERE ID=%s"
    value=(student_id,)

    cursor.execute(query, value)
    result=cursor.fetchall()
    cursor.close()
    conn.close()

    return result

@app.delete("/student/{student_id}")
def remove_students(student_id:int):
    conn=connection()
    cursor=conn.cursor(dictionary=True)

    
    query="DELETE FROM student_info WHERE ID=%s"
    value=(student_id,)
    cursor.execute(query,value)
    
    conn.commit()
    cursor.close()
    conn.close()

    return f"Removed. Check Database."

@app.put("/student/{student_id}")
def update_student_info(student_id:int, data:Student):
    conn=connection()
    cursor=conn.cursor(dictionary=True)

    query="UPDATE student_info SET Semester=%s WHERE ID=%s"
    values=(data.semester,student_id,)

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close() 

    return f"Updated Data. Check Database."

