#Admin screen
import tkinter
from tkinter import ttk
from tkinter import messagebox

import LoginService as serv

class AdminGUI():

    def __init__(self):

        # CONTANTS
        self.PROFESSOR = "PROFESSOR"
        self.STUDENT = "STUDENT"

        # MAIN WINDOW
        self.main_window = tkinter.Tk()
        self.main_window.geometry('300x200')
        self.main_window.title("Admin access")

        #GETTING TYPES
        self.types = serv.getTypes()
        self.types.pop(0)

        #VAR TO SET COMBOBOX VALUE
        self.var = tkinter.StringVar()

        #FRAME AND CANVAS
        self.masterFrame = tkinter.Frame(self.main_window)
        self.canvasStudent = tkinter.Canvas(self.main_window)
        self.frameStd1 = tkinter.Frame(self.canvasStudent)
        self.frameStd2 = tkinter.Frame(self.canvasStudent)
        self.frameStd3 = tkinter.Frame(self.canvasStudent)
        self.frameStd4 = tkinter.Frame(self.canvasStudent)
        self.frameStd5 = tkinter.Frame(self.canvasStudent)
        self.frameStd6 = tkinter.Frame(self.canvasStudent)

        self.canvasProfessor = tkinter.Canvas(self.main_window)
        self.frameProf1 = tkinter.Frame(self.canvasProfessor)


        # SCREEN ELEMENTS
        self.typeUserLabel = tkinter.Label(self.masterFrame, text="Select type user:")
        self.typeEntry = ttk.Combobox(self.masterFrame, textvariable=self.var, values=self.types)
        self.typeEntry.current(0)
        self.typeEntry.bind("<<ComboboxSelected>>", self.toogle_canvas)

        #STUDENT
        self.studentsTitleLabel = tkinter.Label(self.frameStd1, text="Students data")

        #PROFESSOR
        self.professorTitleLabe = tkinter.label(self.frameProf1, text="Professors data")

        #PACK
        self.masterFrame.pack(fill="x")
        self.canvasStudent.pack(fill="x")
        self.frameStd1.pack(fill="x")

        self.studentsTitleLabel.pack(side="left")
        self.typeUserLabel.pack(side="left")
        self.typeEntry.pack(side="left")

        tkinter.mainloop()


    def toogle_canvas(self, event):
        if self.var.get() == self.PROFESSOR:
            self.canvasStudent.pack_forget()
        else:
            self.canvasStudent.pack(fill="x")




adm = AdminGUI()


        