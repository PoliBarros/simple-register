import DataBaseConnection as db
from mysql.connector import Error


class ProfReturn:
    std = ""
    course = ""
    msg = ""


def find_professor(idProf):
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT nameProf FROM Professor WHERE idProf= %s", (idProf,))
        prof = cursor.fetchone()


        if prof is not None:
            return prof
        else:
            return "Professor not found."

    except Error as e:
        print("Error while connecting to MySQL", e)
        return "An error occurred while searching"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")


def find_student(idStd, profId):
    ret = ProfReturn()
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student WHERE idStudents= %s and profIdStd = %s", (idStd, profId))
        std = cursor.fetchall()

        if std is not None:
            #if std.count() > 1:
            courseList = []
            for c in std:
                courseList.append(c[2])

            param = ','.join(['%s'] * len(courseList))
            sql = """SELECT * FROM Course WHERE courseCode IN (%s)"""
            cursor.execute("SELECT * FROM Course WHERE courseCode IN (%s)" % param, tuple(courseList))
            courses = cursor.fetchall()

            ret.std = std[0]
            ret.course = courses
            ret.msg = ""
            return ret
        else:
            ret.std = ""
            ret.course = ""
            ret.msg = "Student not found."
            return ret

    except Error as e:
        print("Error while connecting to MySQL", e)
        ret.result = ""
        ret.msg = "An error occurred while searching"
        return

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")

