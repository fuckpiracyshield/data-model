from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator

from piracyshield_data_model.account.rule import AccountRule

from piracyshield_data_model.account.role.model import AccountRoleModel

class AccountModel(BaseModel):

    """
    Central account data modeling class.
    """

    account_id = None

    name = None

    email = None

    password = None

    role = None

    is_active = True

    def __init__(self, account_id: str, name: str, email: str, password: str, confirm_password: str, role: int, is_active: bool):
        """
        Validates the parameters.

        :param account_id: a valid account identifier.
        :param name: name of the account.
        :param email: e-mail of the account.
        :param password: a valid password.
        :param confirm_password: the exact copy of the password.
        :param role: an int identifying the account role.
        :param is_active: whether the account is active or not.
        """

        self.account_id = self._validate_account_id(account_id)

        self.name = self._validate_name(name)

        self.email = self._validate_email(email)

        self.password = self._validate_password(password)

        self.confirm_password = self._validate_confirm_password(confirm_password)

        self.role = self._validate_role(role)

        self.is_active = self._validate_is_active(is_active)

    def _validate_account_id(self, value: str) -> str | Exception:
        """
        Validates the account identifier.

        :param value: a valid string based on the required rules.
        :return: the same value.
        """

        validator = Validator(value, AccountRule.ACCOUNT_ID)

        validator.validate()

        if not validator.is_valid():
            raise AccountModelAccountIDException(validator.errors)

        return value

    def _validate_name(self, value: str) -> str | Exception:
        """
        Validates the account name.

        :param value: a valid string based on the required rules.
        :return: the same value.
        """

        validator = Validator(value, AccountRule.NAME)

        validator.validate()

        if not validator.is_valid():
            raise AccountModelNameException(validator.errors)

        return value

    def _validate_email(self, value: str) -> str | Exception:
        """
        Validates the account e-mail.

        :param value: a valid string based on the required rules.
        :return: the same value.
        """

        validator = Validator(value, AccountRule.EMAIL)

        validator.validate()

        if not validator.is_valid():
            raise AccountModelEmailException(validator.errors)

        return value

    def _validate_password(self, value: str) -> str | Exception:
        """
        Validates the account password.

        :param value: a valid string based on the required rules.
        :return: the same value.
        """

        validator = Validator(value, AccountRule.PASSWORD)

        validator.validate()

        if not validator.is_valid():
            raise AccountModelPasswordException(validator.errors)

        return value

    def _validate_confirm_password(self, value: str) -> str | Exception:
        """
        Validates the password confirmation.

        :param value: a valid string based on the required rules.
        :return: the same value.
        """

        validator = Validator(value, AccountRule.PASSWORD)

        validator.validate()

        if not validator.is_valid():
            raise AccountModelConfirmPasswordException(validator.errors)

        # finally verify if the two passwords match
        if value != self.password:
            raise AccountModelConfirmPasswordMismatchException(validator.errors)

        return value

    def _validate_role(self, value: int) -> int | Exception:
        """
        Validates the account role identifier.

        :param value: a valid integer based on the required rules.
        :return: the same value.
        """

        validator = Validator(value, AccountRule.ROLE)

        validator.validate()

        if not validator.is_valid():
            raise AccountModelRoleException(validator.errors)

        try:
            enum = AccountRoleModel(value)

            return enum.value

        except ValueError:
            raise AccountModelRoleException()

    def _validate_is_active(self, value: bool) -> bool | Exception:
        """
        Validates the account status.

        :param value: true/false if active or not.
        :return: the same value.
        """

        if isinstance(value, bool):
            return value

        raise AccountModelIsActiveException()

class AccountModelAccountIDException(Exception):

    """
    Non valid account identifier.
    """

    pass

class AccountModelNameException(Exception):

    """
    Non valid name.
    """

    pass

class AccountModelEmailException(Exception):

    """
    Non valid e-mail address.
    """

    pass

class AccountModelPasswordException(Exception):

    """
    Non valid password.
    """

    pass

class AccountModelConfirmPasswordException(Exception):

    """
    Non valid confirm password.
    """

    pass

class AccountModelConfirmPasswordMismatchException(Exception):

    """
    Confirm password differs from password.
    """

    pass

class AccountModelRoleException(Exception):

    """
    Non valid role.
    """

    pass

class AccountModelIsActiveException(Exception):

    """
    Non valid is active value.
    """

    pass
