# Student

import tkinter
from tkinter import ttk

class StudentGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('500x300')
        self.main_window.title("Student access")

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)

        self.topFrame = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.frame3 = tkinter.Frame(self.main_window)
        self.frameTable = tkinter.Frame(self.main_window)

        #ELEMENTS
        self.studentLogged = tkinter.Label(self.frame1, text="Student Logged: ")
        self.studentEntry = tkinter.Entry(self.frame2, width=20)
        self.studentTitle = tkinter.Label(self.frame3, text="Grades", font=("Helvetica", 16))

        #PACK
        self.frame1.pack(fill="x")
        self.frame2.pack(fill="x")

        self.studentLogged.pack(side="left")
        self.studentEntry.pack(side="left", fill="both")

        self.topFrame.pack(fill="x", pady=10)
        self.frame3.pack(fill="x")
        self.frameTable.pack(fill="x", padx=30)
        self.studentTitle.pack(side="left", fill="both", padx=25)


        self.LoadTable()

        tkinter.mainloop()

    def table(self):

        table = ttk.Treeview(self.frameTable)
        table['columns'] = ('course', 'grade')
        table.heading("#0", text='Student', anchor='w')
        table.column("#0", anchor="w")
        table.heading('course', text='Course Name')
        table.column('course', anchor='center', width=100)
        table.heading('grade', text='Grade')
        table.column('grade', anchor='center', width=100)
        table.grid(sticky=("N", "S", "W", "E"))
        table.grid_rowconfigure(0, weight = 1)
        table.grid_columnconfigure(0, weight = 1)
        return table

    def LoadTable(self):
        self.table().insert('', 'end', text="Name goes here", values=('CSAT', '90'))



std = StudentGUI()