import re

from mvc.services.exceptions.invalid_name_exception import InvalidNameException

# todo fix regex
NAME_REGEX = r"[a-zA-z0-9._\\-]{3,}"


class UserDataValidator:
    @staticmethod
    def validate_name(name):
        if not re.match(NAME_REGEX, name):
            raise InvalidNameException()
