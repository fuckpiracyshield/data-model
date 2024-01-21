from piracyshield_data_model.base import BaseModel

class AccountFlagsModel(BaseModel):

    flags = {
        'change_password': False
    }

    def __init__(self, flags: dict):
        # little hack
        self.flags = self.flags

        if not all(flag in self.flags.keys() for flag in flags.keys()):
            raise AccountFlagsModelUnknownFlagException()

        self.flags['change_password'] = self._validate_flag(flags['change_password'])

    def _validate_flag(self, value: bool) -> bool | Exception:
        """
        Validates the single flag value.

        :param value: true/false if the flag is active or not.
        :return: the same value.
        """

        if isinstance(value, bool):
            return value

        raise AccountFlagsModelChangePasswordException()

class AccountFlagsModelUnknownFlagException(Exception):

    """
    Unknown flag.
    """

    pass

class AccountFlagsModelValueException(Exception):

    """
    Non valid value.
    """

    pass
