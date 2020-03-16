#Admin screen
import tkinter
from tkinter import ttk

import LoginService as serv

class AdminGUI():

    def __init__(self):

        # CONTANTS
        self.COURSE = "COURSE"
        self.PROFESSOR = "PROFESSOR"
        self.STUDENT = "STUDENT"

        # MAIN WINDOW
        self.main_window = tkinter.Tk()
        self.main_window.geometry('500x220')
        self.main_window.title("Admin access")

        #GETTING TYPES
        self.types = serv.getTypes()
        self.types.pop(0)

        #VAR TO SET COMBOBOX VALUE
        self.var = tkinter.StringVar()
        self.profCourseVar = tkinter.StringVar()
        self.studentCourseVar = tkinter.StringVar()

        #FRAME AND CANVAS
        self.masterFrame = tkinter.Frame(self.main_window, pady=15)
        self.canvasStudent = tkinter.Canvas(self.main_window)
        self.frameStd1 = tkinter.Frame(self.canvasStudent)
        self.frameStd2 = tkinter.Frame(self.canvasStudent, width="250")
        self.frameStd3 = tkinter.Frame(self.canvasStudent, width="250")
        self.frameStd4 = tkinter.Frame(self.canvasStudent)
        self.frameStd5 = tkinter.Frame(self.canvasStudent)
        self.frameStd6 = tkinter.Frame(self.canvasStudent)
        self.frameStd7 = tkinter.Frame(self.canvasStudent)

        self.topSeparator = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.bottomSeparator = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")

        self.canvasProfessor = tkinter.Canvas(self.main_window)
        self.frameProf1 = tkinter.Frame(self.canvasProfessor)
        self.frameProf2 = tkinter.Frame(self.canvasProfessor)
        self.frameProf3 = tkinter.Frame(self.canvasProfessor)
        self.frameProf4 = tkinter.Frame(self.canvasProfessor)
        self.frameProf5 = tkinter.Frame(self.canvasProfessor)
        self.frameProf6 = tkinter.Frame(self.canvasProfessor)
        self.frameProf7 = tkinter.Frame(self.canvasProfessor)

        self.canvasCourse = tkinter.Canvas(self.main_window)
        self.frameCourse1 = tkinter.Frame(self.canvasCourse)
        self.frameCourse2 = tkinter.Frame(self.canvasCourse)
        self.frameCourse3 = tkinter.Frame(self.canvasCourse)

        self.bottomFrame = tkinter.Frame(self.main_window)


        # SCREEN ELEMENTS
        self.typeUserLabel = tkinter.Label(self.masterFrame, text="Select type user:")
        self.typeEntry = ttk.Combobox(self.masterFrame, textvariable=self.var, values=self.types)
        self.typeEntry.current(0)
        self.typeEntry.bind("<<ComboboxSelected>>", self.toogle_canvas)

        #STUDENT
        self.studentsTitleLabel = tkinter.Label(self.frameStd1, text="Students data", font=("Helvetica", 16))
        self.studentNumberLabel = tkinter.Label(self.frameStd2, text="Student's Number:")
        self.studentNumberEntry = tkinter.Entry(self.frameStd3, width=21)
        self.btnSearchStudent = tkinter.Button(self.frameStd3, text="Search", command="")

        self.studentNameLabel = tkinter.Label(self.frameStd2, text="Student's Name:", padx=122)
        self.studentNameEntry = tkinter.Entry(self.frameStd3, width=20)

        self.studentCourseNameLabel = tkinter.Label(self.frameStd4, text="Student's Course")
        self.studentCourseNameEntry = ttk.Combobox(self.frameStd5, textvariable=self.studentCourseVar,
                                                   values="", width=25)
        #self.studentCourseNameEntry.current(0)

        self.studentGradeLabel = tkinter.Label(self.frameStd4, text="Grade:", padx=129)
        self.studentGradeEntry = tkinter.Entry(self.frameStd5, width=20)

        self.studentUsernameLabel = tkinter.Label(self.frameStd6, text="Username:")
        self.studentUsernameEntry = tkinter.Entry(self.frameStd7, width=26)

        self.studentPasswordLabel = tkinter.Label(self.frameStd6, text="Password:", padx=180)
        self.studentPasswordEntry = tkinter.Entry(self.frameStd7, width=21)

        #PROFESSOR
        self.professorTitleLabel = tkinter.Label(self.frameProf1, text="Professor's data", font=("Helvetica", 16))

        self.professorNumberLabel = tkinter.Label(self.frameProf2, text="Professor's number:")
        self.professorNumberEntry = tkinter.Entry(self.frameProf3, width=20)
        self.btnSearchProf = tkinter.Button(self.frameProf3, text="Search", command="")

        self.professorNameLabel = tkinter.Label(self.frameProf2, text="Professor's Name:", padx=110)
        self.professorNameEntry = tkinter.Entry(self.frameProf3, width=20)

        self.professorCourseLabel = tkinter.Label(self.frameProf4, text="Course:")
        self.professorCourseEntry = ttk.Combobox(self.frameProf5, textvariable=self.profCourseVar, values="")
        #self.professorCourseEntry.current(0)

        self.professorUsernameLabel = tkinter.Label(self.frameProf6, text="Professor's username:")
        self.professorUsernameEntry = tkinter.Entry(self.frameProf7, width=20)

        self.professorPasswordLabel = tkinter.Label(self.frameProf6, text="Professor's password:", padx=40)
        self.professorPasswordEntry = tkinter.Entry(self.frameProf7, width=20)

        #COURSE
        self.courseTitleLabel = tkinter.Label(self.frameCourse1, text="Course", font=("Helvetica", 16))

        self.courseNumberLabel = tkinter.Label(self.frameCourse2, text="Course Number: ")
        self.courseNumberEntry = tkinter.Entry(self.frameCourse3, width=20)
        self.btnSearchCourse = tkinter.Button(self.frameCourse3, text="Search", command="")

        self.courseNameLabel = tkinter.Label(self.frameCourse2, text="Course Number: ", padx=125)
        self.courseNameEntry = tkinter.Entry(self.frameCourse3, width=20)

        #buttons

        self.btnSave = tkinter.Button(self.bottomFrame, text="Save/Update", command="", width=10)
        self.btnDelete = tkinter.Button(self.bottomFrame, text="Delete", command="", width=10)
        self.btnNew = tkinter.Button(self.bottomFrame, text="New", command="", width=10)

        #PACK
        self.masterFrame.pack(fill="x")
        self.topSeparator.pack(fill="x", padx=5, pady=5)
        self.canvasCourse.pack(fill="x")
        self.canvasStudent.pack_forget()
        self.canvasProfessor.pack_forget()

        self.frameStd1.pack(fill="x")
        self.frameStd2.pack(fill="both", expand="true")
        self.frameStd3.pack(fill="both", expand="true")
        self.frameStd4.pack(fill="both", expand="true")
        self.frameStd5.pack(fill="both", expand="true")
        self.frameStd6.pack(fill="both", expand="true")
        self.frameStd7.pack(fill="both", expand="true")

        self.frameProf1.pack(fill="x")
        self.frameProf2.pack(fill="x")
        self.frameProf3.pack(fill="x")
        self.frameProf4.pack(fill="x")
        self.frameProf5.pack(fill="x")
        self.frameProf6.pack(fill="x")
        self.frameProf7.pack(fill="x")

        self.frameCourse1.pack(fill="x")
        self.frameCourse2.pack(fill="x")
        self.frameCourse3.pack(fill="x")

        self.typeUserLabel.pack(side="left")
        self.typeEntry.pack(side="left")

        self.studentsTitleLabel.pack(side="left", pady=5)
        self.studentNumberLabel.pack(side="left", fill="x")
        self.studentNumberEntry.pack(side="left", fill="both")
        self.btnSearchStudent.pack(side="left", fill="both")

        self.studentNameLabel.pack(side="left", fill="x")
        self.studentNameEntry.pack(side="left", fill="both")

        self.studentCourseNameLabel.pack(side="left", fill="x")
        self.studentCourseNameEntry.pack(side="left", fill="x")

        self.studentGradeLabel.pack(side="left", fill="x")
        self.studentGradeEntry.pack(side="left", fill="both")

        self.studentUsernameLabel.pack(side="left", fill="x")
        self.studentUsernameEntry.pack(side="left", fill="both")

        self.studentPasswordLabel.pack(side="left", fill="x")
        self.studentPasswordEntry.pack(side="left", fill="both")

        #professor
        self.professorTitleLabel.pack(side="left", pady=5)
        self.professorNumberLabel.pack(side="left", fill="x")
        self.professorNumberEntry.pack(side="left", fill="both")
        self.btnSearchProf.pack(side="left", fill="both")

        self.professorNameLabel.pack(side="left", fill="x")
        self.professorNameEntry.pack(side="left", fill="both")

        self.professorCourseLabel.pack(side="left", fill="x")
        self.professorCourseEntry.pack(side="left", fill="both")

        self.professorUsernameLabel.pack(side="left", fill="x")
        self.professorUsernameEntry.pack(side="left", fill="both")

        self.professorPasswordLabel.pack(side="left", fill="x")
        self.professorPasswordEntry.pack(side="left", fill="both")

        #course
        self.courseTitleLabel.pack(side="left", pady=5)

        self.courseNumberLabel.pack(side="left", fill="x")
        self.courseNumberEntry.pack(side="left", fill="both")
        self.btnSearchCourse.pack(side="left", fill="both")

        self.courseNameLabel.pack(side="left", fill="x")
        self.courseNameEntry.pack(side="left", fill="both")

        #bottom
        self.bottomSeparator.pack(fill="x", padx=5, pady=5)
        self.bottomFrame.pack(fill="both", padx=50, pady=10)
        self.btnNew.pack(side="right", fill="both")
        self.btnDelete.pack(side="right", fill="both", padx=5)
        self.btnSave.pack(side="right", fill="both")


        tkinter.mainloop()


    def toogle_canvas(self, event):
        if self.var.get() == self.PROFESSOR:
            self.canvasStudent.pack_forget()
            self.canvasCourse.pack_forget()
            self.canvasProfessor.pack(fill="x")

            self.bottomSeparator.pack_forget()
            self.bottomSeparator.pack(fill="x", padx=5, pady=5)

            self.bottomFrame.pack_forget()
            self.bottomFrame.pack(fill="both", padx=50, pady=10)
            self.main_window.geometry("500x320")


        elif self.var.get()==self.COURSE:

            self.canvasStudent.pack_forget()
            self.canvasProfessor.pack_forget()
            self.canvasCourse.pack(fill="x")

            self.bottomSeparator.pack_forget()
            self.bottomSeparator.pack(fill="x", padx=5, pady=5)

            self.bottomFrame.pack_forget()
            self.bottomFrame.pack(fill="both", padx=50, pady=10)
            self.main_window.geometry("500x220")

        else:
            self.canvasStudent.pack(fill="x")
            self.canvasCourse.pack_forget()
            self.canvasProfessor.pack_forget()

            self.bottomSeparator.pack_forget()
            self.bottomSeparator.pack(fill="x", padx=5, pady=5)

            self.bottomFrame.pack_forget()
            self.bottomFrame.pack(fill="both", padx=50, pady=10)
            self.main_window.geometry("500x320")


adm = AdminGUI()


        