from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator

from piracyshield_data_model.whitelist.genre.model import WhitelistGenreModel
from piracyshield_data_model.whitelist.rule import WhitelistRule
from piracyshield_data_model.ticket.rule import TicketRule

class WhitelistModel(BaseModel):

    """
    Whitelist data modeling class.
    """

    genre = None

    value = None

    registrar = None

    as_code = None

    is_active = True

    def __init__(self, genre: str, value: str, is_active: bool, registrar: str = None, as_code: str = None):
        """
        Validates the parameters.

        :param genre: FQDN, IPv4, IPv6 or a CIDR IPv4/IPv6 class.
        :param value: value of the item.
        :param is_active: if the item is already active or not.
        :param registrar: registrar of the FQDN item.
        :param as_code: AS code of the IPv4, IPv6 or CIDR classes.
        """

        match genre:
            case WhitelistGenreModel.FQDN.value:
                self.value = self._validate_fqdn(value)
                self.registrar = self._validate_registrar(registrar)

            case WhitelistGenreModel.IPV4.value:
                self.value = self._validate_ipv4(value)
                self.as_code = self._validate_as_code(as_code)

            case WhitelistGenreModel.IPV6.value:
                self.value = self._validate_ipv6(value)
                self.as_code = self._validate_as_code(as_code)

            case WhitelistGenreModel.CIDR_IPV4.value:
                self.value = self._validate_cidr_ipv4(value)
                self.as_code = self._validate_as_code(as_code)

            case WhitelistGenreModel.CIDR_IPV6.value:
                self.value = self._validate_cidr_ipv6(value)
                self.as_code = self._validate_as_code(as_code)

            case _:
                raise WhitelistModelGenreException()

        self.genre = genre

        self.is_active = is_active

    def _validate_fqdn(self, value: str) -> str | Exception:
        """
        Validates the FQDN.

        :param value: a valid FQDN string.
        :return: the same value.
        """

        if not value or not len(value):
            raise WhitelistModelFQDNMissingException()

        validator = Validator(value, TicketRule.FQDN)

        validator.validate()

        if not validator.is_valid():
            raise WhitelistModelFQDNNonValidException(validator.errors)

        return value

    def _validate_ipv4(self, value: str) -> str | Exception:
        """
        Validates the IPv4.

        :param value: a valid IPv4 string.
        :return: the same value.
        """

        if not value or not len(value):
            raise WhitelistModelIPv4MissingException()

        validator = Validator(value, TicketRule.IPV4)

        validator.validate()

        if not validator.is_valid():
            raise WhitelistModelIPv4NonValidException(validator.errors)

        return value

    def _validate_ipv6(self, value: str) -> str | Exception:
        """
        Validates the IPv6.

        :param value: a valid IPv6 string.
        :return: the same value.
        """

        if not value or not len(value):
            raise WhitelistModelIPv6MissingException()

        validator = Validator(value, TicketRule.IPV6)

        validator.validate()

        if not validator.is_valid():
            raise WhitelistModelIPv6NonValidException(validator.errors)

        return value

    def _validate_cidr_ipv4(self, value: str) -> str | Exception:
        """
        Validates the CIDR IPv4 class.

        :param value: a valid CIDR IPv4 class.
        :return: the same value.
        """

        if not value or not len(value):
            raise WhitelistModelCIDRIPv4MissingException()

        validator = Validator(value, WhitelistRule.CIDR_IPV4)

        validator.validate()

        if not validator.is_valid():
            raise WhitelistModelCIDRIPv4NonValidException(validator.errors)

        return value

    def _validate_cidr_ipv6(self, value: str) -> str | Exception:
        """
        Validates the CIDR IPv6 class.

        :param value: a valid CIDR IPv6 class.
        :return: the same value.
        """

        if not value or not len(value):
            raise WhitelistModelCIDRIPv6MissingException()

        validator = Validator(value, WhitelistRule.CIDR_IPV6)

        validator.validate()

        if not validator.is_valid():
            raise WhitelistModelCIDRIPv6NonValidException(validator.errors)

        return value

    def _validate_registrar(self, value: str) -> str | Exception:
        """
        Validates the registrar of a FQDN item.

        :param value: a valid string.
        :return: the same value.
        """

        if not value or not len(value):
            raise WhitelistModelRegistrarMissingException()

        validator = Validator(value, WhitelistRule.REGISTRAR)

        validator.validate()

        if not validator.is_valid():
            raise WhitelistModelRegistrarNonValidException(validator.errors)

        return value

    def _validate_as_code(self, value: str) -> str | Exception:
        """
        Validates the AS code of an IPv4 or IPv6 item.

        :param value: a valid AS code.
        :return: the same value.
        """

        if not value or not len(value):
            raise WhitelistModelASCodeMissingException()

        validator = Validator(value, WhitelistRule.AS_CODE)

        validator.validate()

        if not validator.is_valid():
            raise WhitelistModelASCodeNonValidException(validator.errors)

        return value

class WhitelistModelRegistrarMissingException(Exception):

    """
    Missing registrar.
    """

    pass

class WhitelistModelASCodeMissingException(Exception):

    """
    Missing AS code.
    """

    pass

class WhitelistModelGenreException(Exception):

    """
    Non valid genre.
    """

    pass

class WhitelistModelFQDNMissingException(Exception):

    """
    No FQDN passed.
    """

    pass

class WhitelistModelFQDNNonValidException(Exception):

    """
    Non valid FQDN.
    """

    pass

class WhitelistModelIPv4MissingException(Exception):

    """
    No IPv4 passed.
    """

    pass

class WhitelistModelIPv4NonValidException(Exception):

    """
    Non valid IPv4.
    """

    pass

class WhitelistModelIPv6MissingException(Exception):

    """
    No IPv6 passed.
    """

    pass

class WhitelistModelIPv6NonValidException(Exception):

    """
    Non valid IPv6.
    """

    pass

class WhitelistModelCIDRIPv4MissingException(Exception):

    """
    No CIDR IPv4 class passed.
    """

    pass

class WhitelistModelCIDRIPv4NonValidException(Exception):

    """
    Non valid CIDR IPv4 class.
    """

    pass

class WhitelistModelCIDRIPv6MissingException(Exception):

    """
    No CIDR IPv6 class passed.
    """

    pass

class WhitelistModelCIDRIPv6NonValidException(Exception):

    """
    Non valid CIDR IPv6 class.
    """

    pass

class WhitelistModelRegistrarNonValidException(Exception):

    """
    Non valid registrar.
    """

    pass

class WhitelistModelASCodeNonValidException(Exception):

    """
    Non valid AS code.
    """

    pass
