from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator
from piracyshield_component.utils.time import Time, TimeFormatException

from piracyshield_data_model.ticket.item.unprocessed.reason.model import TicketItemUnprocessedReasonModel

from piracyshield_data_model.ticket.item.unprocessed.rule import TicketItemUnprocessedRule

from piracyshield_data_model.ticket.item.status.model import TicketItemStatusModel

from piracyshield_data_model.ticket.rule import TicketRule
from piracyshield_data_model.account.rule import AccountRule

class TicketItemUnprocessedModel(BaseModel):

    """
    Ticket item unprocessed data modeling class.
    """

    provider_id = None

    value = None

    status = None

    reason = None

    timestamp = None

    note = None

    def __init__(self, provider_id: str, value: str, reason: str, timestamp: str = None, note: str = None):
        """
        Validates the parameters.

        :param provider_id: an account identifier assigned to the ticket item.
        :param value: a valid FQDN, IPv4 or IPv6.
        :param reason: a predefined reason for the unprocessed status.
        :param timestamp: an optional ISO8601 date.
        :param note: an optional string.
        """

        self.provider_id = self._validate_provider_id(provider_id)

        self.value = self._validate_value(value)

        self.status = TicketItemStatusModel.UNPROCESSED.value

        self.reason = self._validate_reason(reason)

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
            raise TicketItemUnprocessedModelProviderIdentifierMissingException()

        validator = Validator(value, AccountRule.ACCOUNT_ID)

        validator.validate()

        if not validator.is_valid():
            raise TicketItemUnprocessedModelProviderIdentifierException(validator.errors)

        return value

    def _validate_value(self, value: str) -> str | Exception:
        """
        Validates the ticket item value.

        :param value: a valid FQDN, IPv4 or IPv6.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketItemUnprocessedModelValueMissingException()

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
            raise TicketItemUnprocessedModelValueNonValidException()

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

    def _validate_reason(self, value: str) -> int | Exception:
        """
        Validates the reason.

        :param value: a valid predefined reason.
        :return: the same value.
        """

        if not value or not len(value):
            raise TicketItemUnprocessedModelReasonMissingException()

        try:
            enum = TicketItemUnprocessedReasonModel(value)

            return enum.value

        except ValueError:
            raise TicketItemUnprocessedModelReasonNonValidException()

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
            raise TicketItemUnprocessedModelTimestampNonValidException()

    def _validate_note(self, value: str) -> str | Exception:
        """
        Validates the note text.

        :param value: a string.
        :return: the same value.
        """

        validator = Validator(value, TicketItemUnprocessedRule.NOTE)

        validator.validate()

        if not validator.is_valid():
            raise TicketItemUnprocessedModelNoteNonValidException(validator.errors)

        return value

class TicketItemUnprocessedModelProviderIdentifierMissingException(Exception):

    """
    Missing provider account identifier.
    """

    pass

class TicketItemUnprocessedModelProviderIdentifierNonValidException(Exception):

    """
    Non valid provider account idenfitier.
    """

    pass

class TicketItemUnprocessedModelValueMissingException(Exception):

    """
    Missing ticket item value.
    """

    pass

class TicketItemUnprocessedModelValueNonValidException(Exception):

    """
    Non valid ticket item value.
    """

    pass

class TicketItemUnprocessedModelReasonMissingException(Exception):

    """
    Missing reason.
    """

    pass

class TicketItemUnprocessedModelReasonNonValidException(Exception):

    """
    Non valid reason.
    """

    pass

class TicketItemUnprocessedModelTimestampNonValidException(Exception):

    """
    Non valid timestamp.
    """

    pass

class TicketItemUnprocessedModelNoteNonValidException(Exception):

    """
    Non valid note.
    """

    pass
