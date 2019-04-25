from mvc.services.user_data_validator import UserDataValidator


class User:
    name = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        UserDataValidator.validate_name(name)
        self.name = name

