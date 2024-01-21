from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator

from piracyshield_data_model.ticket.error.rule import TicketErrorRule

from piracyshield_data_model.ticket.genre.model import TicketGenreModel

from piracyshield_data_model.ticket.rule import TicketRule

class TicketErrorModel(BaseModel):

    """
    Ticket error data modeling class.
    """

    ticket_error_id = None

    genre = None

    ticket_id = None

    fqdn = []

    ipv4 = []

    ipv6 = []

    def __init__(self, ticket_error_id: str, ticket_id: str, fqdn: list, ipv4: list, ipv6: list):
        """
        Validates the parameters.

        :param ticket_error_id: a valid error ticket identifier.
        :param ticket_id: a valid ticket identifier.
        :param fqdn: a list of FQDN items.
        :param ipv4: a list of IPv4 items.
        :param ipv6: a list of IPv6 items.
        """

        # FQDN, IPv4 and IPv6 should never be all empty
        if not any([bool(fqdn), bool(ipv4), bool(ipv6)]):
            raise TicketErrorModelNoDataException

        self.ticket_error_id = self._validate_ticket_error_id(ticket_error_id)

        # this is an error ticket
        self.genre = TicketGenreModel.ERROR.value

        self.ticket_id = self._validate_ticket_id(ticket_id)

        if fqdn:
            self.fqdn = self._validate_fqdn(fqdn)

        if ipv4:
            self.ipv4 = self._validate_ipv4(ipv4)

        if ipv6:
            self.ipv6 = self._validate_ipv6(ipv6)

    def _validate_ticket_error_id(self, value: str) -> str | Exception:
        """
        Validates the error ticket identifier.

        :param value: a valid error ticket identifier string.
        :return: the same value.
        """

        validator = Validator(value, TicketErrorRule.TICKET_ERROR_ID)

        validator.validate()

        if not validator.is_valid():
            raise TicketErrorModelTicketErrorIdentifierException(validator.errors)

        return value

    def _validate_ticket_id(self, value: str) -> str | Exception:
        """
        Validates the ticket identifier.

        :param value: a valid ticket identifier string.
        :return: the same value.
        """

        validator = Validator(value, TicketRule.TICKET_ID)

        validator.validate()

        if not validator.is_valid():
            raise TicketErrorModelTicketIdentifierException(validator.errors)

        return value

    def _validate_fqdn(self, value: list) -> list | Exception:
        """
        Validates the ticket FQDN list.

        :param value: a list of FQDNs.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketErrorModelFQDNMissingException()

        for item in value:
            validator = Validator(item, TicketRule.FQDN)

            validator.validate()

            if not validator.is_valid():
                raise TicketErrorModelFQDNNonValidException(validator.errors)

        return value

    def _validate_ipv4(self, value: list) -> list | Exception:
        """
        Validates the ticket IPv4 list.

        :param value: a list of IPv4s.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketErrorModelIPv4MissingException()

        for item in value:
            validator = Validator(item, TicketRule.IPV4)

            validator.validate()

            if not validator.is_valid():
                raise TicketErrorModelIPv4NonValidException(validator.errors)

        return value

    def _validate_ipv6(self, value: list) -> list | Exception:
        """
        Validates the ticket IPv6 list.

        :param value: a list of IPv6s.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketErrorModelIPv6MissingException()

        for item in value:
            validator = Validator(item, TicketRule.IPV6)

            validator.validate()

            if not validator.is_valid():
                raise TicketErrorModelIPv6NonValidException(validator.errors)

        return value

class TicketErrorModelNoDataException(Exception):

    """
    No FQDN or IPv4 passed.
    """

    pass

class TicketErrorModelTicketErrorIdentifierException(Exception):

    """
    Non valid error ticket identifier.
    """

    pass

class TicketErrorModelTicketIdentifierException(Exception):

    """
    Non valid ticket identifier.
    """

    pass

class TicketErrorModelFQDNMissingException(Exception):

    """
    No FQDN passed.
    """

    pass

class TicketErrorModelFQDNNonValidException(Exception):

    """
    Non valid FQDN.
    """

    pass

class TicketErrorModelIPv4MissingException(Exception):

    """
    No IPv4 passed.
    """

    pass

class TicketErrorModelIPv4NonValidException(Exception):

    """
    Non valid IPv4.
    """

    pass

class TicketErrorModelIPv6MissingException(Exception):

    """
    No IPv6 passed.
    """

    pass

class TicketErrorModelIPv6NonValidException(Exception):

    """
    Non valid IPv6.
    """

    pass
