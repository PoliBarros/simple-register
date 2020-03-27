#Admin screen
import tkinter
from tkinter import ttk

import  Enums as enum
import LoginService as serv

class AdminGUI():

    def __init__(self, windows):

        # MAIN WINDOW
        self.main_window = windows
        self.main_window.geometry('500x220')
        self.main_window.title("Admin access")

        #GETTING TYPES
        self.types = serv.getTypes()
        self.types.pop(0)

        #VAR TO SET COMBOBOX VALUE
        self.var = tkinter.StringVar()
        self.prof_course_var = tkinter.StringVar()
        self.student_course_var = tkinter.StringVar()

        #FRAME AND CANVAS
        self.master_frame = tkinter.Frame(self.main_window, pady=15)
        self.canvas_student = tkinter.Canvas(self.main_window)
        self.frame_std1 = tkinter.Frame(self.canvas_student)
        self.frame_std2 = tkinter.Frame(self.canvas_student, width="250")
        self.frame_std3 = tkinter.Frame(self.canvas_student, width="250")
        self.frame_std4 = tkinter.Frame(self.canvas_student)
        self.frame_std5 = tkinter.Frame(self.canvas_student)
        self.frame_std6 = tkinter.Frame(self.canvas_student)
        self.frame_std7 = tkinter.Frame(self.canvas_student)

        self.top_separator = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.bottom_separator = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")

        self.canvas_professor = tkinter.Canvas(self.main_window)
        self.frame_prof1 = tkinter.Frame(self.canvas_professor)
        self.frame_prof2 = tkinter.Frame(self.canvas_professor)
        self.frame_prof3 = tkinter.Frame(self.canvas_professor)
        self.frame_prof4 = tkinter.Frame(self.canvas_professor)
        self.frame_prof5 = tkinter.Frame(self.canvas_professor)
        self.frame_prof6 = tkinter.Frame(self.canvas_professor)
        self.frame_prof7 = tkinter.Frame(self.canvas_professor)

        self.canvas_course = tkinter.Canvas(self.main_window)
        self.frame_course1 = tkinter.Frame(self.canvas_course)
        self.frame_course2 = tkinter.Frame(self.canvas_course)
        self.frame_course3 = tkinter.Frame(self.canvas_course)

        self.bottom_frame = tkinter.Frame(self.main_window)


        # SCREEN ELEMENTS
        self.type_user_label = tkinter.Label(self.master_frame, text="Select screen to edit:")
        self.type_entry = ttk.Combobox(self.master_frame, textvariable=self.var, values=self.types)
        self.type_entry.current(0)
        self.type_entry.bind("<<ComboboxSelected>>", self.toogle_canvas)

        #STUDENT
        self.students_title_label = tkinter.Label(self.frame_std1, text="Students data", font=("Helvetica", 16))
        self.student_number_label = tkinter.Label(self.frame_std2, text="Student's Number:")
        self.student_number_entry = tkinter.Entry(self.frame_std3, width=21)
        self.btn_search_student = tkinter.Button(self.frame_std3, text="Search", command="")

        self.student_name_label = tkinter.Label(self.frame_std2, text="Student's Name:", padx=122)
        self.student_name_entry = tkinter.Entry(self.frame_std3, width=20)

        self.student_course_name_label = tkinter.Label(self.frame_std4, text="Student's Course")
        self.student_course_name_entry = ttk.Combobox(self.frame_std5, textvariable=self.student_course_var,
                                                   values="", width=25)
        #self.student_course_name_entry.current(0)

        self.student_grade_label = tkinter.Label(self.frame_std4, text="Grade:", padx=129)
        self.student_grade_entry = tkinter.Entry(self.frame_std5, width=20)

        self.student_username_label = tkinter.Label(self.frame_std6, text="Username:")
        self.student_username_entry = tkinter.Entry(self.frame_std7, width=26)

        self.student_password_label = tkinter.Label(self.frame_std6, text="Password:", padx=180)
        self.student_password_entry = tkinter.Entry(self.frame_std7, width=21)

        #PROFESSOR
        self.professor_title_label = tkinter.Label(self.frame_prof1, text="Professor's data", font=("Helvetica", 16))

        self.professor_number_label = tkinter.Label(self.frame_prof2, text="Professor's number:")
        self.professor_number_entry = tkinter.Entry(self.frame_prof3, width=20)
        self.btn_search_prof = tkinter.Button(self.frame_prof3, text="Search", command="")

        self.professor_name_label = tkinter.Label(self.frame_prof2, text="Professor's Name:", padx=110)
        self.professor_name_entry = tkinter.Entry(self.frame_prof3, width=20)

        self.professor_course_label = tkinter.Label(self.frame_prof4, text="Course:")
        self.professor_course_entry = ttk.Combobox(self.frame_prof5, textvariable=self.prof_course_var, values="")
        #self.professor_course_entry.current(0)

        self.professor_username_label = tkinter.Label(self.frame_prof6, text="Professor's username:")
        self.professor_username_entry = tkinter.Entry(self.frame_prof7, width=20)

        self.professor_password_label = tkinter.Label(self.frame_prof6, text="Professor's password:", padx=40)
        self.professor_password_entry = tkinter.Entry(self.frame_prof7, width=20)

        #COURSE
        self.course_title_label = tkinter.Label(self.frame_course1, text="Course", font=("Helvetica", 16))

        self.course_number_label = tkinter.Label(self.frame_course2, text="Course Number: ")
        self.course_number_entry = tkinter.Entry(self.frame_course3, width=20)
        self.btn_search_course = tkinter.Button(self.frame_course3, text="Search", command="")

        self.course_name_label = tkinter.Label(self.frame_course2, text="Course Number: ", padx=125)
        self.course_name_entry = tkinter.Entry(self.frame_course3, width=20)

        #buttons

        self.btn_save = tkinter.Button(self.bottom_frame, text="Save/Update", command="", width=10)
        self.btn_delete = tkinter.Button(self.bottom_frame, text="Delete", command="", width=10)
        self.btn_new = tkinter.Button(self.bottom_frame, text="New", command="", width=10)

        #PACK
        self.master_frame.pack(fill="x")
        self.top_separator.pack(fill="x", padx=5, pady=5)
        self.canvas_course.pack(fill="x")
        self.canvas_student.pack_forget()
        self.canvas_professor.pack_forget()

        self.frame_std1.pack(fill="x")
        self.frame_std2.pack(fill="both", expand="true")
        self.frame_std3.pack(fill="both", expand="true")
        self.frame_std4.pack(fill="both", expand="true")
        self.frame_std5.pack(fill="both", expand="true")
        self.frame_std6.pack(fill="both", expand="true")
        self.frame_std7.pack(fill="both", expand="true")

        self.frame_prof1.pack(fill="x")
        self.frame_prof2.pack(fill="x")
        self.frame_prof3.pack(fill="x")
        self.frame_prof4.pack(fill="x")
        self.frame_prof5.pack(fill="x")
        self.frame_prof6.pack(fill="x")
        self.frame_prof7.pack(fill="x")

        self.frame_course1.pack(fill="x")
        self.frame_course2.pack(fill="x")
        self.frame_course3.pack(fill="x")

        self.type_user_label.pack(side="left")
        self.type_entry.pack(side="left")

        self.students_title_label.pack(side="left", pady=5)
        self.student_number_label.pack(side="left", fill="x")
        self.student_number_entry.pack(side="left", fill="both")
        self.btn_search_student.pack(side="left", fill="both")

        self.student_name_label.pack(side="left", fill="x")
        self.student_name_entry.pack(side="left", fill="both")

        self.student_course_name_label.pack(side="left", fill="x")
        self.student_course_name_entry.pack(side="left", fill="x")

        self.student_grade_label.pack(side="left", fill="x")
        self.student_grade_entry.pack(side="left", fill="both")

        self.student_username_label.pack(side="left", fill="x")
        self.student_username_entry.pack(side="left", fill="both")

        self.student_password_label.pack(side="left", fill="x")
        self.student_password_entry.pack(side="left", fill="both")

        #professor
        self.professor_title_label.pack(side="left", pady=5)
        self.professor_number_label.pack(side="left", fill="x")
        self.professor_number_entry.pack(side="left", fill="both")
        self.btn_search_prof.pack(side="left", fill="both")

        self.professor_name_label.pack(side="left", fill="x")
        self.professor_name_entry.pack(side="left", fill="both")

        self.professor_course_label.pack(side="left", fill="x")
        self.professor_course_entry.pack(side="left", fill="both")

        self.professor_username_label.pack(side="left", fill="x")
        self.professor_username_entry.pack(side="left", fill="both")

        self.professor_password_label.pack(side="left", fill="x")
        self.professor_password_entry.pack(side="left", fill="both")

        #course
        self.course_title_label.pack(side="left", pady=5)

        self.course_number_label.pack(side="left", fill="x")
        self.course_number_entry.pack(side="left", fill="both")
        self.btn_search_course.pack(side="left", fill="both")

        self.course_name_label.pack(side="left", fill="x")
        self.course_name_entry.pack(side="left", fill="both")

        #bottom
        self.bottom_separator.pack(fill="x", padx=5, pady=5)
        self.bottom_frame.pack(fill="both", padx=50, pady=10)
        self.btn_new.pack(side="right", fill="both")
        self.btn_delete.pack(side="right", fill="both", padx=5)
        self.btn_save.pack(side="right", fill="both")

        tkinter.mainloop()

    def toogle_canvas(self, event):
        if self.var.get() == enum.UserTypes.PROFESSOR.name:
            self.canvas_student.pack_forget()
            self.canvas_course.pack_forget()
            self.canvas_professor.pack(fill="x")

            self.bottom_separator.pack_forget()
            self.bottom_separator.pack(fill="x", padx=5, pady=5)

            self.bottom_frame.pack_forget()
            self.bottom_frame.pack(fill="both", padx=50, pady=10)
            self.main_window.geometry("500x320")


        elif self.var.get()==enum.UserTypes.COURSE.name:

            self.canvas_student.pack_forget()
            self.canvas_professor.pack_forget()
            self.canvas_course.pack(fill="x")

            self.bottom_separator.pack_forget()
            self.bottom_separator.pack(fill="x", padx=5, pady=5)

            self.bottom_frame.pack_forget()
            self.bottom_frame.pack(fill="both", padx=50, pady=10)
            self.main_window.geometry("500x220")

        else:
            self.canvas_student.pack(fill="x")
            self.canvas_course.pack_forget()
            self.canvas_professor.pack_forget()

            self.bottom_separator.pack_forget()
            self.bottom_separator.pack(fill="x", padx=5, pady=5)

            self.bottom_frame.pack_forget()
            self.bottom_frame.pack(fill="both", padx=50, pady=10)
            self.main_window.geometry("500x320")

