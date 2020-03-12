# Login screen

import tkinter
import LoginClass as log
import LoginService as logService

class LoginGUI:
    def __init__(self):
        # Main window.
        self.main_window = tkinter.Tk()
        self.main_window.geometry('200x200')
        self.main_window.title("Login")

        self.retunTypes = logService.getTypes()

        #Frames
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window, height=2, bd=2, relief="sunken")
        self.frame5 = tkinter.Frame(self.main_window)

        typeVar = tkinter.StringVar(self.main_window)
        typeVar.set(self.retunTypes[0])

        #elements
        self.typeUserLabel = tkinter.Label(self.frame1, text="Select type user:")
        self.typeEntry = tkinter.OptionMenu(self.frame1, typeVar, *self.retunTypes)

        #Login data
        self.loginLabel = tkinter.Label(self.frame2, text='Login:')
        self.loginEntry = tkinter.Entry(self.frame2, width=10)

        #Password data
        self.password = tkinter.Label(self.frame3, text='Password:')
        self.pwEntry = tkinter.Entry(self.frame3, width=10)

        #button
        self.btnLogin = tkinter.Button(self.frame5, text="Login")
        self.btnLogin.pack()

        # packs
        self.frame1.pack(fill="x")
        self.frame2.pack(fill="x")
        self.frame3.pack(fill="x")
        self.frame4.pack(fill="x", padx=5, pady=5)
        self.frame5.pack(fill="x")

        self.typeUserLabel.pack(side="left")
        self.typeEntry.pack(side="left")
        self.loginLabel.pack(side="left")
        self.loginEntry.pack(side="left")
        self.password.pack(side="left")
        self.pwEntry.pack(side="left")

        tkinter.mainloop()

loginGui = LoginGUI()




