from typing import Optional
from typing import List
from pydantic import BaseModel
class Student(BaseModel):
    id:Optional[int]
    name:str
    email:str
    section_id:int
    password:str

class Day(BaseModel):
    id:Optional[int]
    std:str
    section:str
    day:str
    period_1:str
    period_2:str
    period_3:str
    period_4:str
    period_5:str
    period_6:str

class TimeTable(BaseModel):
    timetable:List[Day]
                
                