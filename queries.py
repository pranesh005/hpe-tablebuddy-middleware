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
        addStudent(id:"""+str(student.id)+""",name:\""""+student.name+"""\",email:\""""+student.email+"""\",section_id:"""+str(student.section_id)+""",password:\""""+student.password+"""\") 
    }"""
    return addStudentQuery