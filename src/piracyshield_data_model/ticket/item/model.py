from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator

from piracyshield_data_model.ticket.item.rule import TicketItemRule

from piracyshield_data_model.ticket.item.status.model import TicketItemStatusModel
from piracyshield_data_model.ticket.item.genre.model import TicketItemGenreModel

from piracyshield_data_model.ticket.rule import TicketRule
from piracyshield_data_model.account.rule import AccountRule

class TicketItemModel(BaseModel):

    """
    Ticket item data modeling class.
    """

    ticket_id = None

    ticket_item_id = None

    provider_id = None

    value = None

    genre = None

    status = None

    is_active = True

    is_duplicate = False

    is_whitelisted = False

    is_error = False

    settings = None

    def __init__(self,
        ticket_id: str,
        ticket_item_id: str,
        provider_id: str,
        value: str,
        genre: str,
        is_active: bool,
        is_duplicate: bool,
        is_whitelisted: bool,
        is_error: bool
    ):
        """
        Validates the parameters.

        :param ticket_id: a valid ticket identifier.
        :param ticket_item_id: a valid ticket item identifier.
        :param value: a valid FQDN or IPv4.
        :param genre: a valid ticket item type.
        :param provider_id: an account identifier assigned to the ticket item.
        """

        self.ticket_id = self._validate_ticket_id(ticket_id)

        self.ticket_item_id = self._validate_ticket_item_id(ticket_item_id)

        match genre:
            case TicketItemGenreModel.FQDN.value:
                self.genre = TicketItemGenreModel.FQDN.value
                self.value = self._validate_fqdn(value)

            case TicketItemGenreModel.IPV4.value:
                self.genre = TicketItemGenreModel.IPV4.value
                self.value = self._validate_ipv4(value)

            case TicketItemGenreModel.IPV6.value:
                self.genre = TicketItemGenreModel.IPV6.value
                self.value = self._validate_ipv6(value)

            case _:
                raise TicketItemModelGenreNonValidException()

        self.provider_id = self._validate_provider_id(provider_id)

        self.status = TicketItemStatusModel.PENDING.value

        self.is_active = is_active

        self.is_duplicate = is_duplicate

        self.is_whitelisted = is_whitelisted

        self.is_error = is_error

        self.settings = {
            'update_max_time': 172800 # 2 days
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
            raise TicketItemModelTicketIdentifierNonValidException(validator.errors)

        return value

    def _validate_ticket_item_id(self, value: str) -> str | Exception:
        """
        Validates the ticket item identifier.

        :param value: a valid ticket item identifier string.
        :return: the same value.
        """

        validator = Validator(value, TicketItemRule.TICKET_ITEM_ID)

        validator.validate()

        if not validator.is_valid():
            raise TicketItemModelTicketIdentifierNonValidException(validator.errors)

        return value

    def _validate_fqdn(self, value: str) -> list | Exception:
        """
        Validates the FQDN genre.

        :param value: a valid FQDN.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketItemModelFQDNMissingException()

        validator = Validator(value, TicketRule.FQDN)

        validator.validate()

        if not validator.is_valid():
            raise TicketItemModelFQDNNonValidException(validator.errors)

        return value

    def _validate_ipv4(self, value: str) -> list | Exception:
        """
        Validates the IPv4 genre.

        :param value: a valid IPv4.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketItemModelIPv4MissingException()

        validator = Validator(value, TicketRule.IPV4)

        validator.validate()

        if not validator.is_valid():
            raise TicketItemModelIPv4NonValidException(validator.errors)

        return value

    def _validate_ipv6(self, value: str) -> list | Exception:
        """
        Validates the IPv6 genre.

        :param value: a valid IPv6.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketItemModelIPv6MissingException()

        validator = Validator(value, TicketRule.IPV6)

        validator.validate()

        if not validator.is_valid():
            raise TicketItemModelIPv6NonValidException(validator.errors)

        return value

    def _validate_provider_id(self, value: str) -> str | Exception:
        """
        Validates the provider account identifier.

        :param value: a valid account identifier.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketItemModelProviderIdentifierMissingException()

        validator = Validator(value, AccountRule.ACCOUNT_ID)

        validator.validate()

        if not validator.is_valid():
            raise TicketItemModelProviderIdentifierNonValidException(validator.errors)

        return value

class TicketItemModelTicketIdentifierNonValidException(Exception):

    """
    Non valid ticket identifier.
    """

    pass

class TicketItemModelTicketItemIdentifierNonValidException(Exception):

    """
    Non valid ticket item identifier.
    """

    pass

class TicketItemModelGenreNonValidException(Exception):

    """
    Non valid genre.
    """

    pass

class TicketItemModelFQDNMissingException(Exception):

    """
    Missing FQDN.
    """

    pass

class TicketItemModelFQDNNonValidException(Exception):

    """
    Non valid FQDN.
    """

    pass

class TicketItemModelIPv4MissingException(Exception):

    """
    Missing IPv4.
    """

    pass

class TicketItemModelIPv4NonValidException(Exception):

    """
    Non valid IPv4.
    """

    pass

class TicketItemModelIPv6MissingException(Exception):

    """
    Missing IPv6.
    """

    pass

class TicketItemModelIPv6NonValidException(Exception):

    """
    Non valid IPv6.
    """

    pass

class TicketItemModelProviderIdentifierMissingException(Exception):

    """
    Missing provider account identifier.
    """

    pass

class TicketItemModelProviderIdentifierNonValidException(Exception):

    """
    Non valid provider account idenfitier.
    """

    pass
