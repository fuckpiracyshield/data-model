from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator

from piracyshield_data_model.authentication.rule import AuthenticationRule

class AuthenticationModel(BaseModel):

    """
    Authentication data modeling class.
    """

    email = None

    password = None

    def __init__(self, email: str, password: str):
        """
        Validates the parameters.

        :param email: e-mail of the account.
        :param password: a valid password.
        """

        self.email = self._validate_email(email)

        self.password = self._validate_password(password)

    def _validate_email(self, value: str) -> str | Exception:
        """
        Validates the account email.

        :param value: a valid string based on the required rules.
        :return: the same value.
        """

        validator = Validator(value, AuthenticationRule.EMAIL)

        validator.validate()

        if not validator.is_valid():
            raise AuthenticationModelEmailException(validator.errors)

        return value

    def _validate_password(self, value: str) -> str | Exception:
        """
        Validates the account password.

        :param value: a valid string based on the required rules.
        :return: the same value.
        """

        validator = Validator(value, AuthenticationRule.PASSWORD)

        validator.validate()

        if not validator.is_valid():
            raise AuthenticationModelPasswordException(validator.errors)

        return value

class AuthenticationModelEmailException(Exception):

    """
    Non valid e-mail address.
    """

    pass

class AuthenticationModelPasswordException(Exception):

    """
    Non valid password.
    """

    pass
