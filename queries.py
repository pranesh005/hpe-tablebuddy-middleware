def getStudentQuery(id:int):
    studentLoginQuery="""query AllStudents {
        getStudent(id:{id}) {
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