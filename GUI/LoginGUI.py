import tkinter
import LoginService as logService


# Login screen
class LoginGUI:
    def __init__(self):
        # Main window.
        self.main_window = tkinter.Tk()
        self.main_window.geometry('400x150')
        self.main_window.title("Login")

        self.retun_types = logService.getTypes()

        #Frames

        self.frame1 = tkinter.Frame(self.main_window)
        self.separator = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)

        type_var = tkinter.StringVar(self.main_window)
        type_var.set(self.retun_types[0])

        #elements
        self.title_login_Label = tkinter.Label(self.frame1, text="Enter a valid username and password.")

        #Login data
        self.login_label = tkinter.Label(self.frame2, text='Login:')
        self.login_entry = tkinter.Entry(self.frame3, width=20)

        #Password data
        self.password = tkinter.Label(self.frame2, text='Password:')
        self.pw_entry = tkinter.Entry(self.frame3, show="*", width=10)

        #button
        self.btn_login = tkinter.Button(self.frame5, text="Login", command=self.login)
        self.btn_login.pack()

        #error message
        self.error_message_label = tkinter.Label(self.frame6, text="")
        self.error_message_label.pack()

        # packs
        self.frame1.pack(fill="x")
        self.separator.pack(fill="x", padx=5, pady=5)
        self.frame2.pack(fill="x")
        self.frame3.pack(fill="x")
        self.frame4.pack(fill="x", padx=5, pady=5)
        self.frame5.pack(fill="x")
        self.frame6.pack(fill="x")

        self.title_login_Label.pack(side="left", fill="x")

        self.login_label.pack(side="left", fill="x")
        self.login_entry.pack(side="left", fill="both")

        self.password.pack(side="left", fill="x", padx=141)
        self.pw_entry.pack(side="left", fill="both")

        tkinter.mainloop()

    def login(self):
        ret = logService.login(self.login_entry.get(), self.pw_entry.get(), self.main_window)
        if ret:
            self.error_message_label['text'] = ret
            self.error_message_label.pack()


loginGui = LoginGUI()




