from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator

from piracyshield_data_model.dda.rule import DDARule

from piracyshield_data_model.account.rule import AccountRule

class DDAModel(BaseModel):

    """
    DDA data modeling class.
    """

    dda_id = None

    description = None

    instance = None

    account_id = None

    is_active = True

    def __init__(self, dda_id: str, description: str, instance: str, account_id: str, is_active: bool):
        """
        Validates the parameters.

        :param dda_id: a valid DDA identifier.
        :param description: textual description.
        :param instance: DDA instance.
        :param account_id: reporter account assigned to this DDA.
        :param is_active: enable/disable this item.
        """

        self.dda_id = self._validate_dda_id(dda_id)

        self.description = self._validate_description(description)

        self.instance = self._validate_instance(instance)

        self.account_id = self._validate_account_id(account_id)

        self.is_active = is_active

    def _validate_dda_id(self, value: str) -> str | Exception:
        """
        Validates the DDA identifier.

        :param value: a valid DDA identifier string.
        :return: the same value.
        """

        validator = Validator(value, DDARule.DDA_ID)

        validator.validate()

        if not validator.is_valid():
            raise DDAModelDDAIdException(validator.errors)

        return value

    def _validate_description(self, value: str) -> str | Exception:
        """
        Validates description.

        :param value: a valid string.
        :return: the same value.
        """

        if not value or not len(value):
            raise DDAModelDescriptionMissingException()

        validator = Validator(value, DDARule.DESCRIPTION)

        validator.validate()

        if not validator.is_valid():
            raise DDAModelDescriptionNonValidException(validator.errors)

        return value

    def _validate_instance(self, value: str) -> str | Exception:
        """
        Validates DDA instance.

        :param value: the DDA instance.
        :return: the same value.
        """

        if not value or not len(value):
            raise DDAModelInstanceMissingException()

        validator = Validator(value, DDARule.INSTANCE)

        validator.validate()

        if not validator.is_valid():
            raise DDAModelInstanceNonValidException(validator.errors)

        return value

    def _validate_account_id(self, value: str) -> str | Exception:
        """
        Validates account identifier.

        :param value: the account identifier.
        :return: the same value.
        """

        if not value or not len(value):
            raise DDAModelAccountIdMissingException()

        validator = Validator(value, AccountRule.ACCOUNT_ID)

        validator.validate()

        if not validator.is_valid():
            raise DDAModelAccountIdNonValidException(validator.errors)

        return value

class DDAModelDDAIdException(Exception):

    """
    Non valid DDA identifier.
    """

    pass

class DDAModelDescriptionMissingException(Exception):

    """
    No description passed.
    """

    pass

class DDAModelDescriptionNonValidException(Exception):

    """
    Non valid description.
    """

    pass

class DDAModelInstanceMissingException(Exception):

    """
    No DDA instance passed.
    """

    pass

class DDAModelInstanceNonValidException(Exception):

    """
    Non valid DDA instance.
    """

    pass

class DDAModelAccountIdMissingException(Exception):

    """
    Non account identifier passed.
    """

    pass

class DDAModelAccountIdNonValidException(Exception):

    """
    Non valid account identifier.
    """

    pass
