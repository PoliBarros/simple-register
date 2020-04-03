import tkinter
import Enums as enum
import DataBaseConnection as db
import Services.StudentService as stdService

from mysql.connector import Error


def getTypes():
    tp = []
    for types in enum.UserTypes:
        tp.append(types.name)

    return tp


def login(username, password, type, login_main):

    try:
        data = (username, password, type)

        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE username = %s " +
                       "AND password = %s " +
                       "AND type = %s", data)
        result = cursor.fetchone()

        if result is not None:
            types = enum.UserTypes

            if result[3] == "ADM":
                from GUI import AdminGUI as adm

                # close parent before open adm
                login_main.withdraw()
                win = tkinter.Toplevel(login_main)
                adm.AdminGUI(win)

            elif result[3] == types.STUDENT.name:
                stdService.get_std_grades_by_user_id(result[0], login_main)
                return
            else:
                from GUI import ProfessorGUI as prof

                # close parent before open adm
                login_main.withdraw()
                win = tkinter.Toplevel(login_main)
                prof.ProfessorGUI(win, result[0])

        else:
            return "No user found"

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")

