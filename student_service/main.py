from fastapi import FastAPI, Depends, status
from typing import List
from schema import Student
from schema import Partial_Update
from service import StudentService
from db import injection

app=FastAPI()
service=StudentService()

@app.post("/student" , status_code=status.HTTP_201_CREATED)
def enter_data(entries: List[Student], conn=Depends(injection)):
    return service.create(entries, conn)

@app.get("/students")
def show_all(skip:int= 0, limit: int= 10, conn=Depends(injection)):
    return service.fetch_all(conn, skip, limit)

@app.get("/student/{student_id}")
def show_details(student_id:int, conn=Depends(injection)):
    return service.fetch(student_id, conn)
    

@app.delete("/student/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_students(student_id:int, conn=Depends(injection)):
    return service.delete(student_id, conn)

@app.put("/student/{student_id}")
def update_student_info(student_id:int, data:Student, conn=Depends(injection)):
    return service.update(student_id, data, conn)

@app.patch("/student/{student_id}")
def partial_update(student_id:int, data:Partial_Update, conn=Depends(injection)):
    return service.partial_update(student_id, data, conn)