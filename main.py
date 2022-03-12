from urllib import response
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.encoders import jsonable_encoder
import requests
import json
import queries
import models


app = FastAPI()
url = "http://backend.npc203.ml/graphql"


@app.post("/students/login")
def studentLogin(request:models.Student):
    r = requests.post(url, json={"query": queries.getStudentQuery(request.email, request.password)})
    print(r.status_code)
    json_data = json.loads(r.text)
    print(json_data)
    results = json_data["data"]["getStudent"]["student"]
    errors = json_data["data"]["getStudent"]["errors"]
    body = {}
    statusCode = 200
    if results:
        body["message"] = "Login Successfull"
        body["user"] = results
    else:
        body["message"] = "Invalid credentials"
        body["error"] = errors
        statusCode = 404
    return JSONResponse(content=jsonable_encoder(body), status_code=statusCode)


@app.post("/teachers/login")
def teacherLogin():
    pass

@app.post("/admin/login")
def adminLogin():
    pass


@app.post("/admin/addTeacher")
def addTeacher():
    pass


@app.post("/admin/addStudent")
def addStudent(request:models.Student):
    print(queries.getAddStudentQuery(request))
    r = requests.post(url, json={"query": queries.getAddStudentQuery(request)})
    print(r.status_code)
    json_data = json.loads(r.text)
    print(json_data)
    results = json_data["data"]["addStudent"]
    statusCode = 200
    if not results["message"] :
        statusCode = 404
    return JSONResponse(content=jsonable_encoder(results), status_code=statusCode)

@app.post("/admin/bulkAddTeachers")
def bulkAddTeachers():
    pass


@app.post("/admin/bulkAddStudents")
def bulkAddStudents():
    pass


@app.post("/admin/editTeacher")
def editTeacher():
    pass


@app.post("/admin/editStudent")
def editStudent():
    pass


@app.get("/students/timetable/{std}/{section}")
def getStudentTimetable(std: str,section:str):
    r = requests.post(url, json={"query": queries.getStudentQuery(std, section)})
    print(r.status_code)
    json_data = json.loads(r.text)
    print(json_data)
    results = json_data["data"]["getStudent"]["student"]
    errors = json_data["data"]["getStudent"]["errors"]
    body = {}
    statusCode = 200
    if results:
        body["message"] = "Login Successfull"
        body["user"] = results
    else:
        body["message"] = "Invalid credentials"
        body["error"] = errors
        statusCode = 404
    return JSONResponse(content=jsonable_encoder(body), status_code=statusCode)

    # calling graphana api



@app.get("/teachers/timetable/{id}")
def getTeacherTimetable(id: int):
    # calling graphana api
    pass


@app.post("/timetable")
def createTimeTable(request:models.TimeTable):
    objects=[]
    for row in request.timetable:
        ob={
            "std":row.std,
            "section":row.section,
            "day":row.day,
            "period_1":row.period_1,
            "period_2":row.period_2,
            "period_3":row.period_3,
            "period_4":row.period_4,
            "period_5":row.period_5,
            "period_6":row.period_6
        }
        objects.append(ob)

    r = requests.post(url, json={"query": queries.getAddTimetableQuery(objects)})
    print(r.status_code)
    json_data = json.loads(r.text)
    print(json_data)
    results = json_data["data"]["addTimeTable"]
    statusCode = 200
    if not results["message"] :
        statusCode = 404
    return JSONResponse(content=jsonable_encoder(results), status_code=statusCode)
    
