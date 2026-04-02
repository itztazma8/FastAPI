"""Necessary modules"""

from fastapi import FastAPI, Depends, status
from typing import List
from schema import Student
from schema import Partial_Update
from service import StudentService
from db import injection

"""Creating FastAPI instance"""
app=FastAPI()
"""Creating object of class, StudentService(), that contains all the necessary functions"""
service=StudentService()

"""All the functions below are the driver code for REST operations"""

"""Creates new entries inside the database"""
@app.post("/student" , status_code=status.HTTP_201_CREATED)
def enter_data(entries: List[Student], conn=Depends(injection)):
    return service.create(entries, conn)

"""Fetching data all at once"""
@app.get("/students")
def show_all(skip:int= 0, limit: int= 10, conn=Depends(injection)):
    return service.fetch_all(conn, skip, limit)

"""Fetching data by using student ID"""
@app.get("/student/{student_id}")
def show_details(student_id:int, conn=Depends(injection)):
    return service.fetch(student_id, conn)
    
"""Deleting all data of a particular student"""
@app.delete("/student/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_students(student_id:int, conn=Depends(injection)):
    return service.delete(student_id, conn)

"""Updating all the information of a particular student"""
@app.put("/student/{student_id}")
def update_student_info(student_id:int, data:Student, conn=Depends(injection)):
    return service.update(student_id, data, conn)

"""Updating partial data of a given student"""
@app.patch("/student/{student_id}")
def partial_update(student_id:int, data:Partial_Update, conn=Depends(injection)):
    return service.partial_update(student_id, data, conn)