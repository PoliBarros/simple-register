
import tkinter
from tkinter import ttk
import Services.StudentService as stdServ


# Student class

class StudentGUI:
    def __init__(self, window, student):
        self.main_window = window
        self.main_window.geometry('500x400')
        self.main_window.title("Student access")

        self.std_frame1 = tkinter.Frame(self.main_window)
        self.std_frame2 = tkinter.Frame(self.main_window)

        self.std_topFrame = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.std_frame3 = tkinter.Frame(self.main_window)
        self.std_frameTable = tkinter.Frame(self.main_window)
        self.std_frame4 = tkinter.Frame(self.main_window)

        # ELEMENTS
        self.student_logged = tkinter.Label(self.std_frame1, text="Student Logged: ")
        self.student_entry = tkinter.Entry(self.std_frame2, width=20)
        self.student_title = tkinter.Label(self.std_frame3, text="Grades", font=("Helvetica", 16))

        # BUTTOM
        self.exit_btn = tkinter.Button(self.std_frame4, text="Exit", command=self.std_exit, width=10)

        # PACK
        self.std_frame1.pack(fill="x")
        self.std_frame2.pack(fill="x")

        self.student_logged.pack(side="left")
        self.student_entry.pack(side="left", fill="both")

        self.std_topFrame.pack(fill="x", pady=10)
        self.std_frame3.pack(fill="x")
        self.std_frameTable.pack(fill="x", pady=10, padx=30)
        self.std_frame4.pack(fill="x", padx=62)
        self.student_title.pack(side="left", fill="both", padx=25)

        self.exit_btn.pack(side="right", fill="both")

        self.load_table(student)

        tkinter.mainloop()

    def std_exit(self):
        self.main_window.destroy()

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
        table.grid_rowconfigure(0, weight=1)
        table.grid_columnconfigure(0, weight=1)
        return table

    def load_table(self, student):
        if student is not None:
            self.student_entry.insert(0, student[1][1])
            table = self.table()
            for s in student:
                self.student_entry.config(state="readonly")
                self.student_entry.config(foreground="grey")
                table.insert('', 'end', text=s[1], values=(s[2], s[3]))
        else:
            self.table().insert('', 'end', text="There is no grade for this student", values=("", ""))

