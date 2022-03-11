from pydantic import BaseModel
class Student(BaseModel):
    id:int
    name:str
    email:str
    section_id:int
    password:str

