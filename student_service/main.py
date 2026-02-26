from fastapi import FastAPI, Depends
from db_verification import connection
from typing import List
from models.student import Student
from models.student import Partial_Update
from services.student_service import StudentService
from db import injection

app=FastAPI()
service=StudentService()

@app.post("/student")
def enter_data(entries: List[Student], conn=Depends(injection)):
    return service.create(entries, conn)


@app.get("/student/{student_id}")
def show_details(student_id:int, conn=Depends(injection)):
    return service.fetch(student_id, conn)
    

@app.delete("/student/{student_id}")
def remove_students(student_id:int, conn=Depends(injection)):
    return service.delete(student_id, conn)

@app.put("/student/{student_id}")
def update_student_info(student_id:int, data:Student, conn=Depends(injection)):
    return service.update(student_id, data, conn)

@app.patch("/student/{student_id}")
def partial_update(student_id:int, data:Partial_Update, conn=Depends(injection)):
    return service.partial_update(student_id, data, conn)