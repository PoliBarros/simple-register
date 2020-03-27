import tkinter

class ProfessorGUI():
    def __init__(self, window):
        self.main_window = window
        self.main_window.geometry('500x240')
        self.main_window.title("Professor access")

        #VAR TO SET COMBOBOX VALUE
        self.var_student = tkinter.StringVar()
        self.var_course = tkinter.StringVar()

        #FRAMES
        self.professor_frame1 = tkinter.Frame(self.main_window)
        self.professor_frame2 = tkinter.Frame(self.main_window)
        self.professor_frame3 = tkinter.Frame(self.main_window)
        self.professor_frame4 = tkinter.Frame(self.main_window)
        self.professor_frame5 = tkinter.Frame(self.main_window)
        self.professor_frame6 = tkinter.Frame(self.main_window)

        self.professor_top_separator = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.professor_bottom_separator = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")

        self.professor_bottom_frame = tkinter.Frame(self.main_window)

        #ELEMENTS
        self.logged_label = tkinter.Label(self.professor_frame1, text="Logged Professor:")
        self.logged_entry = tkinter.Entry(self.professor_frame2, state="disabled", bg="gray")

        self.student_number_label = tkinter.Label(self.professor_frame3, text="Student No:")
        self.student_number_entry = tkinter.Entry(self.professor_frame4, width=10)
        self.btn_search_student = tkinter.Button(self.professor_frame4, text="Search", command="")

        self.student_name_label = tkinter.Label(self.professor_frame3, text="Student Name:", padx=70)
        self.student_name_entry = tkinter.Entry(self.professor_frame4, width=35)

        self.course_number_label = tkinter.Label(self.professor_frame5, text="Course No:")
        self.course_number_entry = tkinter.Entry(self.professor_frame6, width=10)
        self.btn_search_course = tkinter.Button(self.professor_frame6, text="Search", command="")

        self.course_name_label = tkinter.Label(self.professor_frame5, text="Course Name:", padx=75)
        self.course_name_entry = tkinter.Entry(self.professor_frame6, width=25)

        self.grade_label = tkinter.Label(self.professor_frame5, text="Grade:", padx=77)
        self.grade_entry = tkinter.Entry(self.professor_frame6, width=9)

        #BUTTOM
        self.btn_save = tkinter.Button(self.professor_bottom_frame, text="Save", command="", width=10)
        self.btn_new = tkinter.Button(self.professor_bottom_frame, text="New", command="", width=10)
        self.btn_exit = tkinter.Button(self.professor_bottom_frame, text="Exit", command=self.close_prof, width=10)

        #PACK
        self.professor_frame1.pack(fill="x")
        self.professor_frame2.pack(fill="x")
        self.professor_top_separator.pack(fill="x",  padx=5, pady=10)
        self.professor_frame3.pack(fill="x")
        self.professor_frame4.pack(fill="x")
        self.professor_frame5.pack(fill="x")
        self.professor_frame6.pack(fill="x")

        self.logged_label.pack(side="left", fill="x")
        self.logged_entry.pack(side="left", fill="both")

        self.student_number_label.pack(side="left", fill="x")
        self.student_number_entry.pack(side="left", fill="both")
        self.btn_search_student.pack(side="left", fill="both")

        self.student_name_label.pack(side="left", fill="x")
        self.student_name_entry.pack(side="left", fill="both")

        self.course_number_label.pack(side="left", fill="x")
        self.course_number_entry.pack(side="left", fill="both")
        self.btn_search_course.pack(side="left", fill="both")

        self.course_name_label.pack(side="left", fill="x")
        self.course_name_entry.pack(side="left", fill="both")

        self.grade_label.pack(side="left", fill="x")
        self.grade_entry.pack(side="left", fill="both")

        self.professor_bottom_separator.pack(fill="x",  padx=5, pady=10)
        self.professor_bottom_frame.pack(fill="x", padx=12)

        self.btn_exit.pack(side="right", fill="both")
        self.btn_save.pack(side="right", fill="both")
        self.btn_new.pack(side="right", fill="both", padx=5)

        tkinter.mainloop()

    def close_prof(self):
        self.main_window.destroy()
