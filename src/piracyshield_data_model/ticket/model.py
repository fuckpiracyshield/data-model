from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator

from piracyshield_data_model.ticket.status.model import TicketStatusModel

from piracyshield_data_model.ticket.genre.model import TicketGenreModel

from piracyshield_data_model.account.rule import AccountRule

from piracyshield_data_model.dda.rule import DDARule

from piracyshield_data_model.ticket.rule import TicketRule

class TicketModel(BaseModel):

    """
    Ticket data modeling class.
    """

    ticket_id = None

    genre = None

    description = None

    fqdn = []

    ipv4 = []

    ipv6 = []

    assigned_to = []

    status = None

    settings = None

    def __init__(self, ticket_id: str, dda_id: str, fqdn: list, ipv4: list, ipv6: list, assigned_to: list, description: str = None):
        """
        Validates the parameters.

        :param ticket_id: a valid ticket identifier.
        :param dda_id: a valid DDA identifier.
        :param fqdn: a list of FQDN items.
        :param ipv4: a list of IPv4 items.
        :param ipv6: a list of IPv6 items.
        :param assigned_to: a list of account identifiers assigned to the ticket.
        :param description: a generic, non mandatory, description of the ticket.
        """

        # FQDN, IPv4 and IPv6 should never be all empty
        if not any([bool(fqdn), bool(ipv4), bool(ipv6)]):
            raise TicketModelNoDataException

        self.ticket_id = self._validate_ticket_id(ticket_id)

        self.dda_id = self._validate_dda_id(dda_id)

        if description:
            self.description = self._validate_description(description)

        if fqdn:
            self.fqdn = self._validate_fqdn(fqdn)

        if ipv4:
            self.ipv4 = self._validate_ipv4(ipv4)

        if ipv6:
            self.ipv6 = self._validate_ipv6(ipv6)

        self.assigned_to = self._validate_assigned_to(assigned_to) if assigned_to else None

        # ticket initial status
        self.status = TicketStatusModel.CREATED.value

        # this is a blocking ticket
        self.genre = TicketGenreModel.BLOCKING.value

        self.settings = {
            'autoclose_time': 1875, # 31.25 minutes in seconds, considering 75 seconds of preamble
            'revoke_time': 75,
            'report_error_time': 86400 # 1 day
        }

    def _validate_ticket_id(self, value: str) -> str | Exception:
        """
        Validates the ticket identifier.

        :param value: a valid ticket identifier string.
        :return: the same value.
        """

        validator = Validator(value, TicketRule.TICKET_ID)

        validator.validate()

        if not validator.is_valid():
            raise TicketModelTicketIdException(validator.errors)

        return value

    def _validate_dda_id(self, value: str) -> str | Exception:
        """
        Validates the DDA identifier.

        :param value: a valid DDA identifier string.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketModelDDAIdMissingException()

        validator = Validator(value, DDARule.DDA_ID)

        validator.validate()

        if not validator.is_valid():
            raise TicketModelDDAIdNonValidException(validator.errors)

        return value

    def _validate_description(self, value: str) -> str | Exception:
        """
        Validates the ticket description.

        :param value: a valid string.
        :return: the same value.
        """

        validator = Validator(value, TicketRule.DESCRIPTION)

        validator.validate()

        if not validator.is_valid():
            raise TicketModelDescriptionException(validator.errors)

        return value

    def _validate_fqdn(self, value: list) -> list | Exception:
        """
        Validates the ticket FQDN list.

        :param value: a list of FQDNs.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketModelFQDNMissingException()

        for item in value:
            validator = Validator(item, TicketRule.FQDN)

            validator.validate()

            if not validator.is_valid():
                raise TicketModelFQDNNonValidException(validator.errors)

        return value

    def _validate_ipv4(self, value: list) -> list | Exception:
        """
        Validates the ticket IPv4 list.

        :param value: a list of IPv4s.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketModelIPv4MissingException()

        for item in value:
            validator = Validator(item, TicketRule.IPV4)

            validator.validate()

            if not validator.is_valid():
                raise TicketModelIPv4NonValidException(validator.errors)

        return value

    def _validate_ipv6(self, value: list) -> list | Exception:
        """
        Validates the ticket IPv6 list.

        :param value: a list of IPv6s.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketModelIPv6MissingException()

        for item in value:
            validator = Validator(item, TicketRule.IPV6)

            validator.validate()

            if not validator.is_valid():
                raise TicketModelIPv6NonValidException(validator.errors)

        return value

    def _validate_assigned_to(self, value: list) -> list | Exception:
        """
        Validates the ticket assigned accounts list.

        :param value: a list of account identifiers.
        :return: the same value.
        """

        if not value or not len(value):
            validator = Validator(item, AccountRule.ACCOUNT_ID)

            validator.validate()

            if not validator.is_valid():
                raise TicketModelAssignedToNonValidException(validator.errors)

        return value

class TicketModelNoDataException(Exception):

    """
    No FQDN or IPv4 passed.
    """

    pass

class TicketModelTicketIdException(Exception):

    """
    Non valid ticket identifier.
    """

    pass

class TicketModelDDAIdMissingException(Exception):

    """
    Missing DDA identifier.
    """

    pass

class TicketModelDDAIdNonValidException(Exception):

    """
    Non valid DDA identifier.
    """

    pass

class TicketModelDescriptionException(Exception):

    """
    Non valid description.
    """

    pass

class TicketModelFQDNMissingException(Exception):

    """
    No FQDN passed.
    """

    pass

class TicketModelFQDNNonValidException(Exception):

    """
    Non valid FQDN.
    """

    pass

class TicketModelIPv4MissingException(Exception):

    """
    No IPv4 passed.
    """

    pass

class TicketModelIPv4NonValidException(Exception):

    """
    Non valid IPv4.
    """

    pass

class TicketModelIPv6MissingException(Exception):

    """
    No IPv6 passed.
    """

    pass

class TicketModelIPv6NonValidException(Exception):

    """
    Non valid IPv6.
    """

    pass

class TicketModelAssignedToNonValidException(Exception):

    """
    Non valid account id passed.
    """

    pass
