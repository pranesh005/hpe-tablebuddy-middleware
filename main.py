import json
from io import BytesIO
from lib2to3.pgen2.pgen import DFAState
from urllib import response

import pandas
import requests
from fastapi import FastAPI, File
from fastapi.encoders import jsonable_encoder
from fastapi.requests import Request
from fastapi.responses import JSONResponse

import models
import queries
from generate_timetable import generate, main_lock

app = FastAPI()
base_url = "http://localhost:8000"
url = "http://20.62.141.224:8080/graphql"


@app.post("/admin/addStudent", response_model=models.CommonResponse)
def addStudent(request: models.Student):
    r = requests.post(url, json={"query": queries.addStudentQuery(request)})
    print(r.status_code)
    json_data = json.loads(r.text)
    print(json_data)
    results = json_data["data"]["addStudent"]
    statusCode = 200
    body = {}
    if not results["message"]:
        statusCode = 404
        body["success"] = False
        body["error"] = results["errors"][0]
    else:
        body["success"] = True
        body["message"] = results["message"]
    return JSONResponse(content=jsonable_encoder(body), status_code=statusCode)


@app.post("/students/login", response_model=models.LoginResponse)
def studentLogin(request: models.LoginRequest):
    r = requests.post(
        url, json={"query": queries.getStudentQuery(request.email, request.password)}
    )
    print(r.status_code)
    json_data = json.loads(r.text)
    print(json_data)
    results = json_data["data"]["getStudent"]["student"]
    errors = json_data["data"]["getStudent"]["errors"]
    body = {}
    statusCode = 200
    if results:
        body["success"] = True
        body["message"] = "Login Successfull"
        body["user"] = results
    else:
        body["success"] = False
        body["error"] = errors[0]
        statusCode = 404
    return JSONResponse(content=jsonable_encoder(body), status_code=statusCode)


@app.get("/students/timetable/{std}/{section}", response_model=models.getTimeTableResponse)
def getStudentTimetable(std: str, section: str):
    r = requests.post(url, json={"query": queries.getTimeTableQuery(std, section)})
    print(r.status_code)
    json_data = json.loads(r.text)
    print(json_data)
    results = json_data["data"]["getTimeTable"]["timetable"]
    errors = json_data["data"]["getTimeTable"]["errors"]
    body = {}
    statusCode = 200
    if results:
        body["timetable"] = results
        body["success"] = True
    else:
        body["success"] = False
        body["error"] = errors[0]
        statusCode = 404
    return JSONResponse(content=jsonable_encoder(body), status_code=statusCode)


@app.post("/timetable", response_model=models.CommonResponse)
def createTimeTable(request: models.TimeTable):
    success = True
    for row in request.timetable:
        ob = {
            "std": row.std,
            "section": row.section,
            "day": row.day,
            "p_one": row.p_one,
            "p_two": row.p_two,
            "p_three": row.p_three,
            "p_four": row.p_four,
            "p_five": row.p_five,
            "p_six": row.p_six,
        }

        r = requests.post(url, json={"query": queries.createTimeTableQuery(ob)})
        json_data = json.loads(r.text)
        results = json_data["data"]["createTimeTable"]
        if not results["message"]:
            body = {"success": False, "error": results["errors"][0]}
            success = False
            return JSONResponse(content=jsonable_encoder(body), status_code=404)

    if success:
        body = {"success": True, "message": results["message"]}
        return JSONResponse(content=jsonable_encoder(body), status_code=200)


@app.delete("/timetable/delete")
def deleteTimeTable():
    r = requests.post(url, json={"query": queries.deleteTimeTableQuery()})
    print(r.status_code)
    json_data = json.loads(r.text)
    print(json_data)
    results = json_data["data"]["deleteTimeTable"]
    statusCode = 200
    body = {}
    if not results["message"]:
        body["success"] = False
        body["error"] = results["errors"][0]
        statusCode = 404
    else:
        body["success"] = True
        body["message"] = results["message"]

    return JSONResponse(content=jsonable_encoder(body), status_code=statusCode)


@app.post("/admin/upload_csv")
def load_csv(file: bytes = File(...)):
    df = pandas.read_csv(BytesIO(file))
    for index, row in df.iterrows():
        post_data = {}
        for col in df.columns:
            post_data[col] = row[col]
        requests.post(base_url + "/admin/addStudent", json=post_data)


@app.post("/admin/generate")
def generate_timetable():
    pass


# @app.post("/teachers/login")
# def teacherLogin():
#     pass

# @app.post("/admin/login")
# def adminLogin():
#     pass


# @app.post("/admin/addTeacher")
# def addTeacher():
#     pass


# @app.post("/admin/bulkAddTeachers")
# def bulkAddTeachers():
#     pass


# @app.post("/admin/bulkAddStudents")
# def bulkAddStudents():
#     pass


# @app.post("/admin/editTeacher")
# def editTeacher():
#     pass


# @app.post("/admin/editStudent")
# def editStudent():
#     pass


# @app.get("/teachers/timetable/{id}")
# def getTeacherTimetable(id: int):
#     # calling graphana api
#     pass
