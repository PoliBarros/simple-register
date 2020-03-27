import tkinter
import DataBaseConnection as db

from mysql.connector import Error


def get_std_grades_by_user_id(userId, login_main):

    try:

        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student WHERE userIdStd = %s", (userId, ))
        result = cursor.fetchall()

        from GUI import StudentGUI as std

        # close parent before open adm
        login_main.withdraw()
        win = tkinter.Toplevel(login_main)
        std.StudentGUI(win, result)
        return result

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection is closed")


