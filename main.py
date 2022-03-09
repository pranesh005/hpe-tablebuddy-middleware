from fastapi import FastAPI
import requests
import json
# import pandas as pd
import queries


app=FastAPI()
url="http://dummy.npc203.ml:9021/graphql"


@app.post('/students/login')
def studentLogin():
    print("api called")
    print("query is "+queries.getStudentQuery(1))
    r = requests.post(url, json={'query': queries.getStudentQuery(1)})
    print(r.status_code)
    print(r.text)
    return r.text

@app.post('/teachers/login')
def teacherLogin():
    pass

@app.post('/admin/login')
def teacherLogin():
    pass

@app.post('/admin/addTeacher')
def addTeacher():
    pass

@app.post('/admin/addStudent')
def addStudent():
    pass

@app.post('/admin/bulkAddTeachers')
def bulkAddTeachers():
    pass

@app.post('/admin/bulkAddStudents')
def bulkAddStudents():
    pass

@app.post('/admin/editTeacher')
def editTeacher():
    pass

@app.post('/admin/editStudent')
def editStudent():
    pass

@app.get('/students/timetable/{class_id}')
def getStudentTimetable(class_id:int):
    #calling graphana api
    pass

@app.get('/teachers/timetable/{id}')
def getStudentTimetable(id:int):
    #calling graphana api
    pass

@app.post('/timetable')
def createTimeTable():
    pass

