from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    id: int 
    first_name: str = Field(min_length=3, max_length=150)
    last_name: str = Field(min_length=3, max_length=150)
    semester: int = Field(ge=1, le=10)


class Partial_Update(BaseModel):
    ID:Optional [int]=None
    First_Name: Optional [str]= Field(min_length=3, max_length=150)
    Last_Name:Optional [str]= Field(min_length=3, max_length=150)
    Semester:Optional [int]= Field(ge=1, le=10)

