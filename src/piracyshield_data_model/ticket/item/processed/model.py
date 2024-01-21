from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator
from piracyshield_component.utils.time import Time, TimeFormatException

from piracyshield_data_model.ticket.item.processed.rule import TicketItemProcessedRule

from piracyshield_data_model.ticket.item.status.model import TicketItemStatusModel

from piracyshield_data_model.ticket.rule import TicketRule
from piracyshield_data_model.account.rule import AccountRule

class TicketItemProcessedModel(BaseModel):

    """
    Ticket item processed data modeling class.
    """

    provider_id = None

    value = None

    status = None

    timestamp = None

    note = None

    def __init__(self, provider_id: str, value: str, timestamp: str = None, note: str = None):
        """
        Validates the parameters.

        :param provider_id: an account identifier assigned to the ticket item.
        :param value: a valid FQDN, IPv4 or IPv6.
        :param timestamp: an optional ISO8601 date.
        :param note: an optional string.
        """

        self.provider_id = self._validate_provider_id(provider_id)

        self.value = self._validate_value(value)

        self.status = TicketItemStatusModel.PROCESSED.value

        if timestamp:
            self.timestamp = self._validate_timestamp(timestamp)

        if note:
            self.note = self._validate_note(note)

    def _validate_provider_id(self, value: str) -> str | Exception:
        """
        Validates the provider account identifier.

        :param value: a valid account identifier.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketItemProcessedModelProviderIdentifierMissingException()

        validator = Validator(value, AccountRule.ACCOUNT_ID)

        validator.validate()

        if not validator.is_valid():
            raise TicketItemProcessedModelProviderIdentifierException(validator.errors)

        return value

    def _validate_value(self, value: str) -> str | Exception:
        """
        Validates the ticket item value.

        :param value: a valid FQDN, IPv4 or IPv6.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketItemProcessedModelValueMissingException()

        validators = [
            self._validate_fqdn,
            self._validate_ipv4,
            self._validate_ipv6
        ]

        is_valid = False

        for validator in validators:
            if validator(value):
                is_valid = True

        if not is_valid:
            raise TicketItemProcessedModelValueNonValidException()

        return value

    def _validate_fqdn(self, value: str) -> list | Exception:
        """
        Validates the FQDN genre.

        :param value: a valid FQDN.
        :return: the same value.
        """

        validator = Validator(value, TicketRule.FQDN)

        validator.validate()

        if not validator.is_valid():
            return False

        return value

    def _validate_ipv4(self, value: str) -> list | Exception:
        """
        Validates the IPv4 genre.

        :param value: a valid IPv4.
        :return: the same value.
        """

        validator = Validator(value, TicketRule.IPV4)

        validator.validate()

        if not validator.is_valid():
            return False

        return value

    def _validate_ipv6(self, value: str) -> list | Exception:
        """
        Validates the IPv6 genre.

        :param value: a valid IPv6.
        :return: the same value.
        """

        validator = Validator(value, TicketRule.IPV6)

        validator.validate()

        if not validator.is_valid():
            return False

        return value

    def _validate_timestamp(self, value: str) -> list | Exception:
        """
        Validates the timestamp against the ISO8601 format.

        :param value: a valid ISO8601 date.
        :return: the same value.
        """

        try:
            Time.is_valid_iso8601(value)

            return value

        except TimeFormatException:
            raise TicketItemProcessedModelTimestampNonValidException()

    def _validate_note(self, value: str) -> str | Exception:
        """
        Validates the note text.

        :param value: a string.
        :return: the same value.
        """

        validator = Validator(value, TicketItemProcessedRule.NOTE)

        validator.validate()

        if not validator.is_valid():
            raise TicketItemProcessedModelNoteNonValidException(validator.errors)

        return value

class TicketItemProcessedModelProviderIdentifierMissingException(Exception):

    """
    Missing provider account identifier.
    """

    pass

class TicketItemProcessedModelProviderIdentifierNonValidException(Exception):

    """
    Non valid provider account idenfitier.
    """

    pass

class TicketItemProcessedModelValueMissingException(Exception):

    """
    Missing ticket item value.
    """

    pass

class TicketItemProcessedModelValueNonValidException(Exception):

    """
    Non valid ticket item value.
    """

    pass

class TicketItemProcessedModelTimestampNonValidException(Exception):

    """
    Non valid timestamp.
    """

    pass

class TicketItemProcessedModelNoteNonValidException(Exception):

    """
    Non valid note.
    """

    pass
