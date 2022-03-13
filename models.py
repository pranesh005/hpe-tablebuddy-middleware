from typing import List, Optional
from xmlrpc.client import Boolean

from pydantic import BaseModel


class Student(BaseModel):
    id:Optional[int]
    name:str
    email:str
    section:str
    std:str
    password:str

class LoginResponse(BaseModel):
    message:str
    user:Student
    error:str
    result:bool


class CommonResponse(BaseModel):
    message:str
    success:bool
    error:str

class Day(BaseModel):
    id:Optional[int]
    std:str
    section:str
    day:str
    p_one:str
    p_two:str
    p_three:str
    p_four:str
    p_five:str
    p_six:str

class TimeTable(BaseModel):
    timetable:List[Day]

class LoginRequest(BaseModel):
    email:str
    password:str
class getTimeTableResponse(BaseModel):
    timetable:List[Day]
    success:bool
    error:str
                
                