from datetime import datetime
from ptime import active_time
from threading import Timer


class Start:
    def __init__(self):
        __info_login = [login.isLogin, login.start_date]
        self.prescription = Timer(10, login.check_login)
        while True:
            self.process_section()

    def process_section(self):
        if not login.isLogin:
            print("""
            1: Login
            0: Exit
            """)
        else:
            print("""
            1: Account Info
            2: Active Time
            9: Logout
            0: Logout and Exit
            """)
        section = int(input("select a transaction: "))
        if not login.isLogin:
            if section == 1:
                login.login_process()
                return 0
            elif section == 0:
                self.prescription.cancel()
                exit()
        elif login.isLogin:
            if section == 1:
                login.info_account()
                return 0
            elif section == 2:
                print(active_time(login.start_date))
            elif section == 9:
                login.isLogin = False
            elif section == 0:
                login.logout()


class Login:
    def __init__(self):
        self.isLogin = False
        self.start_date = None

    def login_process(self):
        """
        input for login
        """
        username = input("Username: ")
        password = input("Password: ")
        return self.check_login(username, password)
        # The database will be made later

    def check_login(self, username=None, password=None):
        """
        Login information accuracy check
        """
        # The database will be made later
        if not self.isLogin and username == "admin" and password == "123456":
            return self.complated_login()
        elif self.isLogin:
            return True
        else:
            return self.login_process()

    def complated_login(self):
        """
        Successful entry
        """
        self.isLogin = True
        self.start_date = datetime.now()
        return True

    def auto_logout(self):
        nowtime = datetime.now()
        difference_time = nowtime - self.start_date
        if difference_time.seconds >= 2:
            return exit(self.save_database(self.auto_logout, nowtime, difference_time.seconds))

    def logout(self):
        nowtime = datetime.now()
        difference_time = nowtime - self.start_date
        verification = input("Are you sure(Y/n): ").upper()
        if verification == "Y":
            return exit(self.save_database(self.logout, nowtime, difference_time))
        else:
            return 0

    def save_database(self, function, *word):
        if function.__name__ in ['auto_logout']:
            print(function.__name__, word[0], self.start_date, word[1])
            return Statu_Message(function.__name__)
        return exit()
        # To be added soon

    @staticmethod
    def info_account():
        Statu_Message('info_account')
        return 0

class Statu_Message:
    def __init__(self, function):
        exec(f"self.{function}()")

    @staticmethod
    def auto_logout():
        return print("Automatically logged out")

    @staticmethod
    def logout():
        return print("User logged out")

    @staticmethod
    def info_account():
        return print(f"""
        Login Statu:            {login.isLogin}
        Login Date:             {login.start_date}
        Duration of Activity:   {active_time(login.start_date)}
        """)


login = Login()
