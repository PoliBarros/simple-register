import tkinter
from tkinter import ttk

import Enums as enum
from Services import LoginService as serv
from Services import AdmService as admServ


# Admin screen
class AdminGUI:

    def __init__(self, windows):

        # MAIN WINDOW
        self.main_window = windows
        self.main_window.geometry('500x230')
        self.main_window.title("Admin access")

        # GETTING TYPES
        self.types = serv.getTypes()
        self.types.pop(0)

        # VARIABLES
        self.professor_name_course_student = ""
        self.courses = ""
        self.nameCourse = ""

        # INITIALIZE COURSE COMBOBOX
        self.setAllCourses()

        # VAR TO SET INPUT VALUE
        self.var = tkinter.StringVar()
        self.prof_course_var = tkinter.StringVar()
        self.student_course_var = tkinter.StringVar()
        self.var_numbers = tkinter.StringVar()
        self.student_professor_number = None
        self.var_course_code = tkinter.StringVar()

        # VALIDATIONS
        self.var_numbers.trace('w', self.only_numbers)
        self.var_numbers.trace('w', self.maxlenght)
        self.var_course_code.trace('w', self.maxlenght)

        # FRAME AND CANVAS
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
        self.messageFrame = tkinter.Frame(self.main_window)

        # SCREEN ELEMENTS
        self.type_user_label = tkinter.Label(self.master_frame, text="Select screen to edit:")
        self.type_entry = ttk.Combobox(self.master_frame, textvariable=self.var, values=self.types)
        self.type_entry.current(0)
        self.type_entry.bind("<<ComboboxSelected>>", self.toogle_canvas)

        # STUDENT
        self.students_title_label = tkinter.Label(self.frame_std1, text="Students data", font=("Helvetica", 16), pady=5)
        self.student_number_label = tkinter.Label(self.frame_std2, text="Student's Number:")
        self.student_number_entry = tkinter.Entry(self.frame_std3, width=21, textvariable=self.var_numbers)
        self.btn_search_student = tkinter.Button(self.frame_std3, text="Search", command=self.find)

        self.student_name_label = tkinter.Label(self.frame_std2, text="Student's Name:", padx=122)
        self.student_name_entry = tkinter.Entry(self.frame_std3, width=20)

        self.student_course_name_label = tkinter.Label(self.frame_std4, text="Student's Course")
        self.student_course_name_entry = ttk.Combobox(self.frame_std5, textvariable=self.student_course_var,
                                                      values=self.courses, width=15)
        if self.courses:
            self.student_course_name_entry.current(0)

        self.student_course_name_entry.bind("<<ComboboxSelected>>", self.getNameProfessor)

        self.student_professor_label = tkinter.Label(self.frame_std4, text="Course Professor", padx=40)
        self.student_professor_entry = tkinter.Entry(self.frame_std5, width=20)
        if self.professor_name_course_student:
            self.student_professor_entry.insert(0, self.professor_name_course_student)
            self.student_professor_entry.config(state='readonly')

        self.student_grade_label = tkinter.Label(self.frame_std4, text="Grade:", padx=33)
        self.student_grade_entry = tkinter.Entry(self.frame_std5, width=10)

        self.student_username_label = tkinter.Label(self.frame_std6, text="Username:")
        self.student_username_entry = tkinter.Entry(self.frame_std7, width=26)

        self.student_password_label = tkinter.Label(self.frame_std6, text="Password:", padx=180)
        self.student_password_entry = tkinter.Entry(self.frame_std7, width=21)

        # PROFESSOR
        self.professor_title_label = tkinter.Label(self.frame_prof1, text="Professor's data", font=("Helvetica", 16),
                                                   pady=5)

        self.professor_number_label = tkinter.Label(self.frame_prof2, text="Professor's number:")
        self.professor_number_entry = tkinter.Entry(self.frame_prof3, width=20, textvariable=self.var_numbers)
        self.btn_search_prof = tkinter.Button(self.frame_prof3, text="Search", command=self.find)

        self.professor_name_label = tkinter.Label(self.frame_prof2, text="Professor's Name:", padx=110)
        self.professor_name_entry = tkinter.Entry(self.frame_prof3, width=20)

        self.professor_course_label = tkinter.Label(self.frame_prof4, text="Course:")
        self.professor_course_entry = ttk.Combobox(self.frame_prof5, state="readonly",
                                                   textvariable=self.prof_course_var, values=self.courses)
        if self.nameCourse:
            self.professor_course_entry.current(0)

        self.professor_course_name_entry = tkinter.Entry(self.frame_prof5, width=20)
        if self.nameCourse:
            self.professor_course_name_entry.insert(0, self.nameCourse)
            self.professor_course_name_entry.config(state='readonly')

        self.professor_username_label = tkinter.Label(self.frame_prof6, text="Professor's username:")
        self.professor_username_entry = tkinter.Entry(self.frame_prof7, width=20)

        self.professor_password_label = tkinter.Label(self.frame_prof6, text="Professor's password:", padx=40)
        self.professor_password_entry = tkinter.Entry(self.frame_prof7, width=20)

        # Bind
        self.professor_course_entry.bind("<<ComboboxSelected>>", self.select_course)

        # COURSE
        self.course_title_label = tkinter.Label(self.frame_course1, text="Course", font=("Helvetica", 16), pady=5)

        self.course_code_label = tkinter.Label(self.frame_course2, text="Course Code: ")
        self.course_code_entry = tkinter.Entry(self.frame_course3, textvariable=self.var_course_code, width=20)
        self.btn_search_course = tkinter.Button(self.frame_course3, text="Search", command=self.find)

        self.course_name_label = tkinter.Label(self.frame_course2, text="Course Name: ", padx=150)
        self.course_name_entry = tkinter.Entry(self.frame_course3, width=20)

        # BUTTONS
        self.btn_save = tkinter.Button(self.bottom_frame, text="Save/Update", command=self.save, width=10)
        self.btn_delete = tkinter.Button(self.bottom_frame, text="Delete", command=self.delete, width=10)
        self.btn_new = tkinter.Button(self.bottom_frame, text="New", command=self.new, width=10)

        # MESSAGE ERROR
        self.message = tkinter.Label(self.messageFrame, text="", fg="red")

        # PACK
        self.master_frame.pack(fill="x")
        self.top_separator.pack(fill="x", padx=5)
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

        self.students_title_label.pack(side="left")
        self.student_number_label.pack(side="left", fill="x")
        self.student_number_entry.pack(side="left", fill="both")
        self.btn_search_student.pack(side="left", fill="both")

        self.student_name_label.pack(side="left", fill="x")
        self.student_name_entry.pack(side="left", fill="both")

        self.student_course_name_label.pack(side="left", fill="x")
        self.student_course_name_entry.pack(side="left", fill="both")

        self.student_professor_label.pack(side="left", fill="x")
        self.student_professor_entry.pack(side="left", fill="both")

        self.student_grade_label.pack(side="left", fill="x")
        self.student_grade_entry.pack(side="left", fill="both")

        self.student_username_label.pack(side="left", fill="x")
        self.student_username_entry.pack(side="left", fill="both")

        self.student_password_label.pack(side="left", fill="x")
        self.student_password_entry.pack(side="left", fill="both")

        # professor
        self.professor_title_label.pack(side="left")
        self.professor_number_label.pack(side="left", fill="x")
        self.professor_number_entry.pack(side="left", fill="both")
        self.btn_search_prof.pack(side="left", fill="both")

        self.professor_name_label.pack(side="left", fill="x")
        self.professor_name_entry.pack(side="left", fill="both")

        self.professor_course_label.pack(side="left", fill="x")
        self.professor_course_entry.pack(side="left", fill="both")

        self.professor_course_name_entry.pack(side="left", fill="both")

        self.professor_username_label.pack(side="left", fill="x")
        self.professor_username_entry.pack(side="left", fill="both")

        self.professor_password_label.pack(side="left", fill="x")
        self.professor_password_entry.pack(side="left", fill="both")

        # course
        self.course_title_label.pack(side="left")

        self.course_code_label.pack(side="left", fill="x")
        self.course_code_entry.pack(side="left", fill="both")
        self.btn_search_course.pack(side="left", fill="both")

        self.course_name_label.pack(side="left", fill="x")
        self.course_name_entry.pack(side="left", fill="both")

        # bottom
        self.bottom_separator.pack(fill="x", padx=5, pady=5)
        self.bottom_frame.pack(fill="both", padx=50, pady=10)
        self.btn_new.pack(side="right", fill="both")
        self.btn_delete.pack(side="right", fill="both", padx=5)
        self.btn_save.pack(side="right", fill="both")

        self.messageFrame.pack(fill="x")
        self.message.pack(fill="both")

        tkinter.mainloop()

    def getNameProfessor(self, *event):
        if self.student_course_var.get():
            prof = admServ.find_professor_by_course(self.student_course_var.get())
            if prof.result:
                self.student_professor_number = prof.result[0]
                self.student_professor_entry.config(state='normal')
                self.student_professor_entry.delete(0, 'end')
                self.student_professor_entry.insert(0, prof.result[1])
                self.student_professor_entry.config(state='readonly')
            else:
                # clean the field
                self.student_professor_entry.config(state='normal')
                self.student_professor_entry.delete(0, 'end')
                self.student_professor_entry.config(state='readonly')


    def setAllCourses(self):
        # get all course's code
        self.courses = admServ.find_course(None)
        self.courses = self.courses.result
        if self.courses:
            # find the first name of the course for prof
            self.nameCourse = admServ.find_course(self.courses[0])
            self.nameCourse = self.nameCourse.result[1]
            # find professor's name
            prof = admServ.find_professor_by_course(self.courses[0])
            if prof.result:
                # name of professor's course
                self.professor_name_course_student = prof.result[1]

        else:
            self.nameCourse = ""

    def maxlenght(self, *args):
        if self.var.get() == enum.UserTypes.STUDENT.name:
            value = self.var_numbers.get()
            if len(value) > 6:
                self.var_numbers.set(value[:6])
        elif self.var.get() == enum.UserTypes.COURSE.name:
            value = self.var_course_code.get()
            if len(value) > 5:
                self.var_course_code.set(value[:5])
        else:
            value = self.var_numbers.get()
            if len(value) > 4:
                self.var_numbers.set(value[:4])

    def only_numbers(self, *char):
        if not self.var_numbers.get().isdigit():
            corrected = ''.join(filter(str.isdigit, self.var_numbers.get()))
            self.var_numbers.set(corrected)

    def select_course(self, event):
        course = admServ.find_course(self.prof_course_var.get())
        if course.result is not None:
            self.professor_course_name_entry.config(state='normal')
            self.professor_course_name_entry.delete(0, 'end')
            self.professor_course_name_entry.insert(0, course.result[1])
            self.professor_course_name_entry.config(state='readonly')

    def toogle_canvas(self, *event):
        self.new()
        self.setAllCourses()
        # update combobox course of screens
        self.student_course_name_entry.config(values=self.courses)
        self.professor_course_entry.config(values=self.courses)
        if self.var.get() == enum.UserTypes.PROFESSOR.name:
            self.canvas_student.pack_forget()
            self.canvas_course.pack_forget()
            self.canvas_professor.pack(fill="x")
            self.professor_course_name_entry.insert(0, self.nameCourse)

            self.bottom_separator.pack_forget()
            self.bottom_separator.pack(fill="x", padx=5, pady=5)

            self.bottom_frame.pack_forget()
            self.bottom_frame.pack(fill="both", padx=50)
            self.messageFrame.pack_forget()
            self.messageFrame.pack(fill="x")

            self.main_window.geometry("500x330")

        elif self.var.get() == enum.UserTypes.COURSE.name:
            self.canvas_student.pack_forget()
            self.canvas_professor.pack_forget()
            self.canvas_course.pack(fill="x")

            self.bottom_separator.pack_forget()
            self.bottom_separator.pack(fill="x", padx=5, pady=5)

            self.bottom_frame.pack_forget()
            self.bottom_frame.pack(fill="both", padx=50)
            self.messageFrame.pack_forget()
            self.messageFrame.pack(fill="x")

            self.main_window.geometry("500x230")

        else:
            self.canvas_student.pack(fill="x")
            self.canvas_course.pack_forget()
            self.canvas_professor.pack_forget()
            self.student_professor_entry.insert(0, self.professor_name_course_student)

            self.bottom_separator.pack_forget()
            self.bottom_separator.pack(fill="x", padx=5, pady=5)

            self.bottom_frame.pack_forget()
            self.bottom_frame.pack(fill="both", padx=50, pady=10)
            self.messageFrame.pack_forget()
            self.messageFrame.pack(fill="x")

            self.main_window.geometry("500x320")

    def save(self):
        self.message['text'] = ""
        number = self.course_code_entry.get()
        course = self.course_name_entry.get()

        if self.var.get() == enum.UserTypes.COURSE.name:
            if number:
                course = admServ.save_course(number, course)
                self.message['text'] = course
            else:
                self.message['text'] = "Please enter all fields to save."

        elif self.var.get() == enum.UserTypes.PROFESSOR.name:
            number = self.professor_number_entry.get()
            name = self.professor_name_entry.get()
            course = self.professor_course_entry.get()
            username = self.professor_username_entry.get()
            password = self.professor_password_entry.get()
            type = self.var.get()

            if number and name and course and username and password:
                prof = admServ.save_professor(number, name, course, username, password, type)
                if prof.msg:
                    self.message['text'] = prof.msg
            else:
                self.message['text'] = "Please enter all fields to save."

        else:
            stdNumber = self.student_number_entry.get()
            stdName = self.student_name_entry.get()
            stdCourse = self.student_course_var.get()
            stdGrade = self.student_grade_entry.get()
            stdUser = self.student_number_entry.get()
            stdUsername = self.student_username_entry.get()
            stdPassword = self.student_password_entry.get()
            type = self.var.get()
            idProf = self.student_professor_number
            if stdNumber and stdName and stdCourse and stdUsername and stdPassword:
                std = admServ.save_student(stdNumber, stdName, stdCourse, stdGrade,
                                           stdUser, stdUsername, stdPassword, type, idProf)
                self.message['text'] = std
            else:
                self.message['text'] = "Please enter all fields to save."

    def find(self):
        if self.var.get() == enum.UserTypes.COURSE.name:
            self.course_name_entry.insert(0, "")
            course = admServ.find_course(self.course_code_entry.get())
            if course.result is not "":
                self.course_name_entry.insert(0, course.result[1])
            if course.msg is not None:
                self.message['text'] = course.msg

        elif self.var.get() == enum.UserTypes.PROFESSOR.name:

            prof = admServ.find_professor(self.professor_number_entry.get())
            course = admServ.find_course(prof.result[2])
            user = admServ.find_user(self.professor_number_entry.get())

            # clear all fields
            self.new()
            if prof.result is not "":
                self.professor_number_entry.insert(0, prof.result[0])
                self.professor_name_entry.insert(0, prof.result[1])
                self.prof_course_var.set(prof.result[2])
                self.professor_course_name_entry.insert(0, course.result[1])
                self.professor_username_entry.insert(0, user.result[1])
                self.professor_password_entry.insert(0, user.result[2])

            if prof.msg is not None:
                self.message['text'] = prof.msg

        else:
            self.student_name_entry.delete(0, 'end')
            std = admServ.find_student(self.student_number_entry.get())
            user = admServ.find_user(self.student_number_entry.get())
            # clear all fields
            self.new()
            if std.result is not '':
                self.student_number_entry.insert(0, std.result[0])
                self.student_name_entry.insert(0, std.result[1])
                if std.result[5]:
                    prof = admServ.find_professor(std.result[5])
                if std.result[3]:
                    self.student_grade_entry.insert(0, std.result[3])
                if prof:
                    self.student_professor_entry.insert(0, prof.result[1])
                    # set variable value
                    self.student_professor_number = prof.result[0]

                self.student_course_var.set(std.result[2])
                self.student_username_entry.insert(0, user.result[1])
                self.student_password_entry.insert(0, user.result[2])

            if std.msg is not None:
                self.message['text'] = std.msg

    def delete(self):
        self.message['text'] = ""
        if self.var.get() == enum.UserTypes.COURSE.name:
            number = self.course_code_entry.get()
            if number != '':
                course = admServ.delete_course(number)
                if course.msg:
                    self.message['text'] = course.msg
            else:
                self.message['text'] = "Please insert course number to delete."

        elif self.var.get() == enum.UserTypes.PROFESSOR.name:
            prof_number = self.professor_number_entry.get()
            prof_course = self.prof_course_var.get()

            if prof_number != '' and prof_course != '':
                prof = admServ.delete_professor(prof_number, prof_course)
                if prof.msg:
                    self.message['text'] = prof.msg
            else:
                self.message['text'] = "Please insert professor number and course to delete."

        else:
            stdNumber = self.student_number_entry.get()
            if stdNumber != '' and self.var.get() == enum.UserTypes.STUDENT.name:
                student = admServ.delete_student(stdNumber)
                if student.msg:
                    self.message['text'] = student.msg
            else:
                self.message['text'] = "Please insert course number to delete."

    def new(self):
        self.message['text'] = ""

        if self.var.get() == enum.UserTypes.COURSE.name:
            self.course_code_entry.delete(0, 'end')
            self.course_name_entry.delete(0, 'end')

        elif self.var.get() == enum.UserTypes.PROFESSOR.name:
            self.professor_number_entry.delete(0, 'end')
            self.professor_name_entry.delete(0, 'end')
            if self.courses:
                self.professor_course_entry.current(0)
            self.professor_course_name_entry.delete(0, 'end')
            self.professor_username_entry.delete(0, 'end')
            self.professor_password_entry.delete(0, 'end')

        else:
            self.student_number_entry.delete(0, 'end')
            self.student_name_entry.delete(0, 'end')
            self.student_grade_entry.delete(0, 'end')
            if self.courses:
                self.student_course_name_entry.current(0)
            self.student_password_entry.delete(0, 'end')
            self.student_username_entry.delete(0, 'end')
