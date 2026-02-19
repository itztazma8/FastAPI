from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    semester: int


class Partial_Update(BaseModel):
    ID:Optional [int]=None
    First_Name: Optional [str]=None
    Last_Name:Optional [str]=None
    Semester:Optional [int]=None

