import tkinter
import Enums as enum
import DataBaseConnection as db
import Services.StudentService as stdService

from mysql.connector import Error


class AdmReturn:
    result = "",
    msg = ""

def save_course(code, name):
    try:
        data = (code, name)

        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT grade FROM STUDENT WHERE courseCodeStd= %s", (code, ))
        student = cursor.fetchone()

        cursor.execute("SELECT * FROM COURSE WHERE courseCode= %s", (code, ))
        course = cursor.fetchone()

        if course is not None:
            if student is None:
                cursor.execute("UPDATE Course SET courseCode = %s, courseName = %s", data)
                conn.commit()
                return "Course updated"

            else:
                return "This course cannot be updated because is linked to a student grade."

        else:
            cursor.execute("INSERT INTO Course (courseCode, courseName) VALUES(%s,%s)", data)
            conn.commit()
            return "Course saved"

    except Error as e:
        print("Error while connecting to MySQL", e)
        return "An error occurred while saving"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")


def find_course(code):

    try:
        conn = db.connect()
        cursor = conn.cursor()
        if code is not None:
            cursor.execute("SELECT * FROM COURSE WHERE courseCode= %s", (code, ))
            course = cursor.fetchone()

            ret = AdmReturn()
            if course is not None:
                ret.result = course
                ret.msg = ""
                return ret
            else:
                ret.result = ""
                ret.msg = "Course not found"
                return ret
        else:
            cursor.execute("SELECT * FROM COURSE")
            course = cursor.fetchall()
            courses = []
            ret = AdmReturn()

            if course is not None:
                for cor in course:
                    courses.append(cor[0])

                ret.result = courses
                ret.msg = ""
                return ret
            else:
                ret = AdmReturn()
                ret.result = ""
                ret.msg = "Course not found"
                return ret

    except Error as e:
        print("Error while connecting to MySQL", e)
        return "An error occurred while searching"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")


def delete_course(code):
    try:

        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT grade FROM Student WHERE courseCodeStd= %s", (code, ))
        student = cursor.fetchone()

        ret = AdmReturn()

        if student is None:
            cursor.execute("DELETE FROM Course WHERE courseCode = %s", (code, ))
            conn.commit()
            ret.result = ""
            ret.msg = "Course successfully deleted!"
        else:
            ret.result = ""
            ret.msg = "This course can't be deleted! Students have been graded."

    except Error as e:
        print("Error while connecting to MySQL", e)
        return "An error occurred while deleting"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")

# ****************** Student **************

def save_student(idStudents, studentName, courseCodeStd, grade, userIdStd):
    try:
        data = (idStudents, studentName, courseCodeStd, grade, userIdStd)

        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STUDENT WHERE idStudents= %s", (idStudents, ))
        student = cursor.fetchone()

        if student is None:
            cursor.execute("INSERT INTO Student (idStudents, studentName, courseCodeStd,"
                           + " grade, userIdStd) VALUES(%s,%s,%s,%s,%s)", data)
            conn.commit()
            return "Student saved."

        else:
            if student[3] is None or student[3] == "":
                cursor.execute("UPDATE Student SET idStudents = %s , studentName = %s, "
                               + "courseCodeStd = %s, grade = %s, userIdStd = %s", data)
                conn.commit()
                return "Student updated."
            else:
                return "Can't be updated. This student was graded."

    except Error as e:
        print("Error while connecting to MySQL", e)
        return "An error occurred while saving"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")

def find_student(idStd):

    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student WHERE idStudents= %s", (idStd, ))
        std = cursor.fetchone()

        ret = AdmReturn()
        if std is not None:
            ret.result = std
            ret.msg = ""
            return ret
        else:
            ret.result = ""
            ret.msg = "Student not found."
            return ret

    except Error as e:
        print("Error while connecting to MySQL", e)
        return "An error occurred while searching"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")


def delete_student(code):
    try:

        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT grade FROM Student WHERE idStudents= %s", (code, ))
        student = cursor.fetchone()

        ret = AdmReturn()

        if student is None:
            cursor.execute("DELETE FROM Student WHERE idStudents = %s", (code, ))
            conn.commit()
            ret.result = ""
            ret.msg = "Student successfully deleted!"
        else:
            ret.result = ""
            ret.msg = "Can't be deleted! This student was already graded."

    except Error as e:
        print("Error while connecting to MySQL", e)
        return "An error occurred while deleting"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")

# ****************** Professor **************

def save_professor(idProf, nameProf, courseCodeProf, usename, password):
    try:

        data_user = (idProf, usename, password, enum.UserTypes.PROFESSOR.name)
        data_prof = (idProf, nameProf, courseCodeProf, idProf)

        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Professor WHERE idProf= %s", (idProf, ))
        professor = cursor.fetchone()

        if professor is None:
            cursor.execute("INSERT INTO User (userId, username, password, type) VALUES(%s,%s,%s,%s)", data_user)
            conn.commit()

            cursor.execute("INSERT INTO Professor (idProf, nameProf, courseCodeProf,"
                           + " userIdProf) VALUES(%s,%s,%s,%s)", data_prof)
            conn.commit()
            return "Professor saved"

        else:
            cursor.execute("SELECT grade FROM Student WHERE courseCodeStd= %s", (courseCodeProf,))
            student = cursor.fetchone()
            ret = AdmReturn()

            if student is not None:

                cursor.execute("SELECT * FROM Professor WHERE courseCodeProf= %s"
                               + " and idProf = %s", (courseCodeProf, idProf))
                prof = cursor.fetchone()

                if prof is None:
                    cursor.execute("UPDATE Professor SET idProf = %s , nameProf = %s, "
                               + "courseCodeProf = %s, userIdProf = %s", data_prof)
                    conn.commit()
                    return "Professor updated"
                else:
                    return "Can be updated. This professor is linked with a student grade."
            else:
                cursor.execute("UPDATE Professor SET idProf = %s , nameProf = %s, "
                               + "courseCodeProf = %s, userIdProf = %s", data_prof)
                conn.commit()
                return "Professor updated"

    except Error as e:
        conn.rollback()
        print("Error while connecting to MySQL", e)
        return "An error occurred while saving"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")

def find_professor(idProf):

    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Professor WHERE idProf= %s", (idProf, ))
        prof = cursor.fetchone()

        ret = AdmReturn()
        if prof is not None:
            ret.result = prof
            ret.msg = ""
            return ret
        else:
            ret.result = ""
            ret.msg = "Professor not found."
            return ret

    except Error as e:
        print("Error while connecting to MySQL", e)
        return "An error occurred while searching"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")


def delete_professor(idProf, codeCourse):
    try:

        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT grade FROM Student WHERE courseCodeStd= %s", (codeCourse, ))
        student = cursor.fetchone()
        ret = AdmReturn()

        if student is not None:

            cursor.execute("SELECT * FROM Professor WHERE courseCodeProf= %s and idProf = %s", (codeCourse, idProf))
            prof = cursor.fetchone()

            if prof is None:
                cursor.execute("DELETE FROM Professor WHERE idProf = %s and courseCodeProf= %s", (idProf, codeCourse))
                conn.commit()
                ret.result = ""
                ret.msg = "Professor successfully deleted!"
            else:
                ret.result = ""
                ret.msg = "Can't be deleted! This professor is linked to a grade student."
        else:
            cursor.execute("DELETE FROM Professor WHERE idProf = %s and courseCodeProf= %s", (idProf, codeCourse))
            conn.commit()
            ret.result = ""
            ret.msg = "Professor successfully deleted!"

    except Error as e:
        print("Error while connecting to MySQL", e)
        return "An error occurred while deleting"

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")
