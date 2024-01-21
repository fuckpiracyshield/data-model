from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator

from piracyshield_data_model.ticket.rule import TicketRule

from piracyshield_data_model.log.rule import LogRule

class LogTicketModel(BaseModel):

    """
    Ticket logging data modeling class.
    """

    ticket_id = None

    message = None

    def __init__(self, ticket_id: str, message: str):
        """
        Validates the parameters.

        :param identifier: a valid identifier that represent the service object of the logging.
        :param message: value of the item.
        """

        self.ticket_id = self._validate_ticket_id(ticket_id)

        self.message = self._validate_message(message)

    def _validate_ticket_id(self, value: str) -> str | Exception:
        """
        Validates the ticket identifier.

        :param value: a valid ticket identifier string.
        :return: the same value.
        """

        validator = Validator(value, TicketRule.TICKET_ID)

        validator.validate()

        if not validator.is_valid():
            raise LogTicketModelTicketIdentifierNonValidException(validator.errors)

        return value

    def _validate_message(self, value: str) -> str | Exception:
        """
        Validates the message.

        :param value: a valid message string.
        :return: the same value.
        """

        validator = Validator(value, LogRule.MESSAGE)

        validator.validate()

        if not validator.is_valid():
            raise LogTicketModelMessageNonValidException(validator.errors)

        return value

class LogTicketModelTicketIdentifierMissingException(Exception):

    """
    Missing ticket identifier.
    """

    pass

class LogTicketModelTicketIdentifierNonValidException(Exception):

    """
    Non valid ticket identifier.
    """

    pass

class LogTicketModelMessageMissingException(Exception):

    """
    Missing message.
    """

    pass

class LogTicketModelMessageNonValidException(Exception):

    """
    Non valid message.
    """

    pass
