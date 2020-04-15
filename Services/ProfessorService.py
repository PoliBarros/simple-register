import DataBaseConnection as db
from mysql.connector import Error


class ProfReturn:
    std = ""
    course = ""
    msg = ""


def find_professor(idProf):
    try:
        conn = db.connect()
        cursor = conn.conn.cursor()
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
        if conn.conn.is_connected():
            cursor.close()
            conn.conn.close()
            print("Connection is closed")


def find_student(idStd, profId):
    ret = ProfReturn()
    try:
        conn = db.connect()
        cursor = conn.conn.cursor()
        cursor.execute("SELECT * FROM Student WHERE idStudents= %s and profIdStd = %s", (idStd, profId))
        std = cursor.fetchall()

        if std.__len__()> 0:
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
        if conn.conn.is_connected():
            cursor.close()
            conn.conn.close()
            print("Connection is closed")


def find_course(code):
    ret = ProfReturn()
    try:
        conn = db.connect()
        cursor = conn.conn.cursor()
        if code is not None:
            cursor.execute("SELECT courseName FROM Course WHERE courseCode= %s", (code,))
            course = cursor.fetchone()

            cursor.execute("SELECT grade FROM Student WHERE courseCodeStd= %s", (code,))
            std = cursor.fetchone()
            if course is not None:
                ret.std = std
                ret.course = course
                return ret
            else:
                ret.msg = "Course not found"
                return ret

    except Error as e:
        print("Error while connecting to MySQL", e)
        ret.msg = "Course not found"
        return ret

    finally:
        if conn.conn.is_connected():
            cursor.close()
            conn.conn.close()
            print("Connection is closed")


def save(stdId, grade, course):
    ret = ProfReturn()
    data = (grade, stdId, course)

    try:
        conn = db.connect()
        cursor = conn.conn.cursor()
        if stdId and grade and course:
            cursor.execute("UPDATE Student SET grade = %s WHERE profIdStd = %s AND courseCodeStd = %s", data)
            conn.conn.commit()

            ret.msg = "Grade updated"
            return ret

    except Error as e:
        print("Error while connecting to MySQL", e)
        ret.msg = "Error while updating"
        return ret

    finally:
        if conn.conn.is_connected():
            cursor.close()
            conn.conn.close()
            print("Connection is closed")



