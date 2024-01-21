from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator

from piracyshield_data_model.forensic.status.model import ForensicArchiveStatusModel

from piracyshield_data_model.ticket.rule import TicketRule
from piracyshield_data_model.forensic.archive.rule import ForensicArchiveRule

class ForensicArchiveModel(BaseModel):

    """
    Forensic evidence data modeling class.

    This class refers to the physical forensic evidence archive.
    """

    ticket_id = None

    name = None

    status = None

    def __init__(self, ticket_id: str, name: str):
        """
        Validates the parameters.

        :param ticket_id: a valid ticket identifier.
        :param archive_name: the name of the archive.
        """

        self.ticket_id = self._validate_ticket_id(ticket_id)

        self.name = self._validate_name(name)

        self.status = ForensicArchiveStatusModel.SCHEDULED.value

    def _validate_ticket_id(self, value: str) -> str | Exception:
        """
        Validates the ticket identifier.

        :param value: a valid ticket identifier string.
        :return: the same value.
        """

        validator = Validator(value, TicketRule.TICKET_ID)

        validator.validate()

        if not validator.is_valid():
            raise ForensicModelForensicIDException(validator.errors)

        return value

    def _validate_name(self, value: str) -> str | Exception:
        """
        Validates the ticket identifier.

        :param archive_name: a valid string containing only the name of the archive.
        :return: the same value.
        """

        validator = Validator(value, ForensicArchiveRule.NAME)

        validator.validate()

        if not validator.is_valid():
            raise ForensicArchiveModelNameException(validator.errors)

        return value

class ForensicArchiveModelTicketIDException(Exception):

    """
    Non valid ticket identifier.
    """

    pass


class ForensicArchiveModelNameException(Exception):

    """
    Non valid archive name.
    """

    pass
