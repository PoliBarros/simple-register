import tkinter

class ProfessorGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('500x240')
        self.main_window.title("Professor access")

        #VAR TO SET COMBOBOX VALUE
        self.varStudent = tkinter.StringVar()
        self.varCourse = tkinter.StringVar()

        #FRAMES
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)

        self.topSeparator = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.bottomSeparator = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")

        self.bottomFrame = tkinter.Frame(self.main_window)

        #ELEMENTS
        self.loggedLabel = tkinter.Label(self.frame1, text="Logged Professor:")
        self.loggedEntry = tkinter.Entry(self.frame2, state="disabled", bg="gray")

        self.studentNumberLabel = tkinter.Label(self.frame3, text="Student No:")
        self.studentNumberEntry = tkinter.Entry(self.frame4, width=10)
        self.btnSearchStudent = tkinter.Button(self.frame4, text="Search", command="")

        self.studentNameLabel = tkinter.Label(self.frame3, text="Student Name:", padx=70)
        self.studentNameEntry = tkinter.Entry(self.frame4, width=35)

        self.courseNumberLabel = tkinter.Label(self.frame5, text="Course No:")
        self.courseNumberEntry = tkinter.Entry(self.frame6, width=10)
        self.btnSearchCourse = tkinter.Button(self.frame6, text="Search", command="")

        self.courseNameLabel = tkinter.Label(self.frame5, text="Course Name:", padx=75)
        self.courseNameEntry = tkinter.Entry(self.frame6, width=25)

        self.gradeLabel = tkinter.Label(self.frame5, text="Grade:", padx=77)
        self.gradeEntry = tkinter.Entry(self.frame6, width=9)

        #BUTTOM
        self.btnSave = tkinter.Button(self.bottomFrame, text="Save", command="", width=10)
        self.btnNew = tkinter.Button(self.bottomFrame, text="New", command="", width=10)
        self.btnExit = tkinter.Button(self.bottomFrame, text="Exit", command="", width=10)

        #PACK
        self.frame1.pack(fill="x")
        self.frame2.pack(fill="x")
        self.topSeparator.pack(fill="x",  padx=5, pady=10)
        self.frame3.pack(fill="x")
        self.frame4.pack(fill="x")
        self.frame5.pack(fill="x")
        self.frame6.pack(fill="x")

        self.loggedLabel.pack(side="left", fill="x")
        self.loggedEntry.pack(side="left", fill="both")

        self.studentNumberLabel.pack(side="left", fill="x")
        self.studentNumberEntry.pack(side="left", fill="both")
        self.btnSearchStudent.pack(side="left", fill="both")

        self.studentNameLabel.pack(side="left", fill="x")
        self.studentNameEntry.pack(side="left", fill="both")

        self.courseNumberLabel.pack(side="left", fill="x")
        self.courseNumberEntry.pack(side="left", fill="both")
        self.btnSearchCourse.pack(side="left", fill="both")

        self.courseNameLabel.pack(side="left", fill="x")
        self.courseNameEntry.pack(side="left", fill="both")

        self.gradeLabel.pack(side="left", fill="x")
        self.gradeEntry.pack(side="left", fill="both")

        self.bottomSeparator.pack(fill="x",  padx=5, pady=10)
        self.bottomFrame.pack(fill="x", padx=12)

        self.btnExit.pack(side="right", fill="both")
        self.btnNew.pack(side="right", fill="both", padx=5)
        self.btnSave.pack(side="right", fill="both")

        tkinter.mainloop()


prof = ProfessorGUI()

