from mvc.models.user import User
from mvc.services.exceptions.invalid_name_exception import InvalidNameException


class App:
    @staticmethod
    def start():
        a_user = User()

        print("enter a username")
        name = input()

        try:
            a_user.set_name(name)
            print("correct name: " + a_user.get_name())
        except InvalidNameException:
            print("incorrect name: " + a_user.get_name())


app = App()
app.start()
