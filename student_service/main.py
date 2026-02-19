from fastapi import FastAPI
from db_verification import connection
from typing import List
from models.student import Student
from models.student import Partial_Update
from services.student_service import StudentService

app=FastAPI()
service=StudentService()

@app.post("/student")
def enter_data(entries: List[Student]):
    return service.create(entries)


@app.get("/student/{student_id}")
def show_details(student_id:int):
    return service.fetch(student_id)
    

@app.delete("/student/{student_id}")
def remove_students(student_id:int):
    return service.delete(student_id)

@app.put("/student/{student_id}")
def update_student_info(student_id:int, data:Student):
    return service.update(student_id, data)

@app.patch("/student/{student_id}")
def partial_update(student_id:int, data:Partial_Update):
    return service.partial_update(student_id, data)