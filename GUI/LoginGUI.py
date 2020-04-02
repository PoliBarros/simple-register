import tkinter
from Services import LoginService as logService

from tkinter import ttk


# Login screen
class LoginGUI:
    def __init__(self):
        # Main window.
        self.main_window = tkinter.Tk()
        self.main_window.geometry('400x180')
        self.main_window.title("Login")

        self.return_types = logService.getTypes()
        self.return_types.pop(1)

        self.var_type = tkinter.StringVar()

        # Frames

        self.frame0 = tkinter.Frame(self.main_window, height=2)
        self.frame1 = tkinter.Frame(self.main_window)
        self.separator = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)

        type_var = tkinter.StringVar(self.main_window)
        type_var.set(self.return_types[0])

        # elements
        self.title_login_Label = tkinter.Label(self.frame0, text="Select a type and enter a valid username and password.")

        # Type selection
        self.type_label = tkinter.Label(self.frame1, text="Select the type: ")
        self.type_entry = ttk.Combobox(self.frame1, textvariable=self.var_type, values=self.return_types)
        self.type_entry.current(0)

        # Login data
        self.login_label = tkinter.Label(self.frame2, text='Login:')
        self.login_entry = tkinter.Entry(self.frame3, width=20)

        # Password data
        self.password = tkinter.Label(self.frame2, text='Password:')
        self.pw_entry = tkinter.Entry(self.frame3, show="*", width=10)

        # button
        self.btn_login = tkinter.Button(self.frame5, text="Login")
        self.btn_login.pack()

        #error message
        self.error_message_label = tkinter.Label(self.frame6, fg="red", text="")
        self.error_message_label.pack_forget()

        # packs
        self.frame0.pack(fill="x")
        self.frame1.pack(fill="x")
        self.separator.pack(fill="x", padx=5, pady=5)
        self.frame2.pack(fill="x")
        self.frame3.pack(fill="x")
        self.frame4.pack(fill="x", padx=5, pady=5)
        self.frame5.pack(fill="x")
        self.frame6.pack(fill="x")

        self.title_login_Label.pack(side="left", fill="x")

        self.type_label.pack(side="left", fill="x")
        self.type_entry.pack(side="left", fill="both")

        self.login_label.pack(side="left", fill="x")
        self.login_entry.pack(side="left", fill="both")

        self.password.pack(side="left", fill="x", padx=141)
        self.pw_entry.pack(side="left", fill="both")

        # Bind
        self.login_entry.bind("<FocusIn>", self.handle_focus)
        self.pw_entry.bind("<FocusIn>", self.handle_focus)
        self.main_window.bind('<Return>', self.login)
        self.btn_login.bind('<Button-1>', self.login)

        tkinter.mainloop()

    def login(self, event):

        if self.login_entry.get() is not "" and self.pw_entry.get() is not "":
            ret = logService.login(self.login_entry.get(), self.pw_entry.get(), self.var_type.get(), self.main_window)
            if ret:
                self.error_message_label['text'] = ret
                self.error_message_label.pack()

                self.login_entry['text'] = ""
                self.pw_entry['text'] = ""
        else:
            self.error_message_label['text'] = "Please enter username and password"
            self.error_message_label.pack()

    def handle_focus(self, event):
        if event.widget == self.pw_entry or event.widget == self.login_entry:
            self.error_message_label['text'] = ""
            self.error_message_label.pack_forget()


loginGui = LoginGUI()




