from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator

from piracyshield_data_model.ticket.item.rule import TicketItemRule

from piracyshield_data_model.log.rule import LogRule

class LogTicketItemModel(BaseModel):

    """
    Ticket item logging data modeling class.
    """

    ticket_item_id = None

    message = None

    def __init__(self, ticket_item_id: str, message: str):
        """
        Validates the parameters.

        :param ticket_item_id: a valid ticket item identifier.
        :param message: value of the item.
        """

        self.ticket_item_id = self._validate_ticket_item_id(ticket_item_id)

        self.message = self._validate_message(message)

    def _validate_ticket_item_id(self, value: str) -> str | Exception:
        """
        Validates the ticket item identifier.

        :param value: a valid ticket item identifier string.
        :return: the same value.
        """

        if not value or not len(value):
            raise LogTicketItemModelTicketItemIdentifierMissingException()

        validator = Validator(value, TicketItemRule.TICKET_ITEM_ID)

        validator.validate()

        if not validator.is_valid():
            raise LogTicketItemModelTicketItemIdentifierNonValidException(validator.errors)

        return value

    def _validate_message(self, value: str) -> str | Exception:
        """
        Validates the message.

        :param value: a valid message string.
        :return: the same value.
        """

        if not value or not len(value):
            raise LogTicketItemModelMessageMissingException()

        validator = Validator(value, LogRule.MESSAGE)

        validator.validate()

        if not validator.is_valid():
            raise LogTicketItemModelMessageNonValidException(validator.errors)

        return value

class LogTicketItemModelTicketItemIdentifierMissingException(Exception):

    """
    Missing ticket item identifier.
    """

    pass

class LogTicketItemModelTicketItemIdentifierNonValidException(Exception):

    """
    Non valid ticket item identifier.
    """

    pass

class LogTicketItemModelMessageMissingException(Exception):

    """
    Missing message.
    """

    pass

class LogTicketItemModelMessageNonValidException(Exception):

    """
    Non valid message.
    """

    pass
