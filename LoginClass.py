#Login screen
import enum
class LoginClass:
    def __init__(self, login, password):
        self.login = login
        self.password = password

        def getLogin(self):
            return self.login

        def getPassword(self):
            return self.password

        def setLogin(self, login):
            self.login = login

        def setPassword(self, password):
            self.password = password


class UserTypes(enum.Enum):
    ADM = 0
    COURSE = 1
    STUDENTS = 2
    PROFESSOR = 3