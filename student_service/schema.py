from pydantic import BaseModel, Field
from typing import Optional

"""Schema used for updating fully in PUT.
The function is also used for POST as well"""
class Student(BaseModel):
    id: int 
    first_name: str = Field(min_length=3, max_length=150)
    last_name: str = Field(min_length=3, max_length=150)
    semester: int = Field(ge=1, le=10)

"""This is only used for the only one issue,
which is PATCH as the update must be partial
barring the ID, which must only be changed
if the particular student does not exist"""

class Partial_Update(BaseModel):
    ID: Optional[int]=None
    First_Name: Optional[str] = Field(None, min_length=3, max_length=150)
    Last_Name: Optional[str] = Field(None, min_length=3, max_length=150)
    Semester: Optional[int] = Field(None, ge=1, le=10)
