class InvalidNameException(Exception):
    @staticmethod
    def get_message(name):
        return "incorrect name: " + name
    pass
