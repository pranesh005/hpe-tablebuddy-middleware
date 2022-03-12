import models
def getStudentQuery(email:str,password:str):
    studentLoginQuery="""query AllStudents {
        getStudent(email:"""+email+""",password:"""+password+""") {
            errors
            student {
                id
                name
                email
                section_id
                password
            }
        }
    }"""

    return studentLoginQuery

def getAddStudentQuery(student:models.Student):
    addStudentQuery="""mutation {
        addStudent(name:\""""+student.name+"""\",email:\""""+student.email+"""\",section_id:"""+str(student.section_id)+""",password:\""""+student.password+"""\") {message errors}
    }"""
    return addStudentQuery
# def getAddTimetableQuery(timetable:models.TimeTable):
#     addTimeTableQuery="""mutation {
#         addTimeTable(std:\""""+timetable.std+"""\",section:\""""+timetable.section+"""\",day:\""""+str(timetable.day)+"""\",period_1:\""""+str(timetable.period_1)+"""\",period_2:\""""+str(timetable.period_2)+"""\",period_3:\""""+str(timetable.period_3)+"""\",period_4:\""""+str(timetable.period_4)+"""\",period_5:\""""+str(timetable.period_5)+"""\",period_6:\""""+timetable.period_6+"""\") {message errors}
#     }"""
#     return addTimeTableQuery

def getAddTimetableQuery(timetable:models.TimeTable):
    print(timetable)
    addTimeTableQuery="""mutation {
        addTimeTable(\"objects\":"""+timetable+""") {message errors}
    }"""
    return addTimeTableQuery

def getTimeTableQuery(std:str,section:str):
    getTimeTable = """query AllStudents {
        getTimeTable(std:"""+std+""",section:"""+section+""") {
            errors
            timetable {
                id
                std
                section
                day
                period_1
                period_2
                period_3
                period_4
                period_5
                period_6
            }
        }
    }"""
    return getTimeTable