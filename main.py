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
    results = json_data["data"]["addStudent"]['message']
    errors = json_data["data"]["addStudent"]['errors']
    body = {}
    statusCode = 200
    if results:
        body["message"] = results
      
    else:
        body["message"] = errors
        statusCode = 404
    return JSONResponse(content=jsonable_encoder(body), status_code=statusCode)

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


@app.get("/students/timetable/{class_id}")
def getStudentTimetable(class_id: int):
    # calling graphana api
    pass


@app.get("/teachers/timetable/{id}")
def getTeacherTimetable(id: int):
    # calling graphana api
    pass


@app.post("/timetable")
def createTimeTable():
    pass
