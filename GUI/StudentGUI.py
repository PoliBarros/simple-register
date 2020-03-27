
import tkinter
from tkinter import ttk


# Student class

class StudentGUI():
    def __init__(self, window):
        self.main_window = window
        self.main_window.geometry('500x400')
        self.main_window.title("Student access")

        self.std_frame1 = tkinter.Frame(self.main_window)
        self.std_frame2 = tkinter.Frame(self.main_window)

        self.std_topFrame = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.std_frame3 = tkinter.Frame(self.main_window)
        self.std_frameTable = tkinter.Frame(self.main_window)

        # ELEMENTS
        self.student_logged = tkinter.Label(self.std_frame1, text="Student Logged: ")
        self.student_entry = tkinter.Entry(self.std_frame2, width=20)
        self.student_title = tkinter.Label(self.std_frame3, text="Grades", font=("Helvetica", 16))

        # PACK
        self.std_frame1.pack(fill="x")
        self.std_frame2.pack(fill="x")

        self.student_logged.pack(side="left")
        self.student_entry.pack(side="left", fill="both")

        self.std_topFrame.pack(fill="x", pady=10)
        self.std_frame3.pack(fill="x")
        self.std_frameTable.pack(fill="x", padx=30)
        self.student_title.pack(side="left", fill="both", padx=25)

        self.LoadTable()

        tkinter.mainloop()

    def table(self):

        table = ttk.Treeview(self.std_frameTable)
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

