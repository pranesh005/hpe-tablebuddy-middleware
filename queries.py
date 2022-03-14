import models


def getStudentQuery(email:str,password:str):
    studentLoginQuery="""query AllStudents {
        getStudent(email:\""""+email+"""\",password:\""""+password+"""\") {
            errors
            student {
                id
                name
                email
                section
                std
                password
            }
        }
    }"""

    return studentLoginQuery

def addStudentQuery(student:models.Student):
    addStudentQuery="""mutation {
        addStudent(name:\""""+student.name+"""\",email:\""""+student.email+"""\",section:\""""+str(student.section)+"""\",std:\""""+str(student.std)+"""\",password:\""""+student.password+"""\") {message errors}
    }"""
    return addStudentQuery
def createTimeTableQuery(timetable:models.Day):
    addTimeTableQuery="""mutation {
        createTimeTable(std:\""""+timetable["std"]+"""\",section:\""""+timetable["section"]+"""\",day:\""""+str(timetable["day"])+"""\",p_one:\""""+str(timetable["p_one"])+"""\",p_two:\""""+str(timetable["p_two"])+"""\",p_three:\""""+str(timetable["p_three"])+"""\",p_four:\""""+str(timetable["p_four"])+"""\",p_five:\""""+str(timetable["p_five"])+"""\",p_six:\""""+timetable["p_six"]+"""\") {message errors}
    }"""
    return addTimeTableQuery

def getTimeTableQuery(std:str,section:str):
    getTimeTable = """query TimeTable {
        getTimeTable(std:"""+std+""",section:"""+section+""") {
            errors
            timetable {
                id
                std
                section
                day
                p_one
                p_two
                p_three
                p_four
                p_five
                p_six
            }
        }
    }"""
    return getTimeTable

def deleteTimeTableQuery():
    return """mutation TimeTable {
        deleteTimeTable {
      			success
            message 
        }
    }"""

def getTeacherTimeTableQuery(std:str,subject:str):
    return """query TeacherTable{
  getTeacherTimeTable(std:"""+std+""",subject:"""+subject+"""){
    errors
    success
    timetable
  }
}
"""
