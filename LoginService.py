import tkinter
import LoginClass as log
import DataBaseConnection as db

from mysql.connector import Error


def getTypes():
    tp = []
    for types in log.UserTypes:
        tp.append(types.name)

    return tp


def login(username, password, login_main):

    try:
        data = (username, password)

        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE username = %s AND password = %s", data)
        result = cursor.fetchone()

        if result is not None:
            types = log.UserTypes

            if result[3] == "ADM":
                import AdminGUI as adm

                # close parent before open adm
                login_main.withdraw()
                win = tkinter.Toplevel(login_main)
                adm.AdminGUI(win)

            elif result[3] == types.STUDENT.name:
                import StudentGUI as std

                # close parent before open adm
                login_main.withdraw()
                win = tkinter.Toplevel(login_main)
                std.StudentGUI(win)
            else:
                import ProfessorGUI as prof

                # close parent before open adm
                login_main.withdraw()
                win = tkinter.Toplevel(login_main)
                prof.ProfessorGUI(win)

        else:
            return "No user found"

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")

