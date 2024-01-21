from enum import Enum

class TicketStatusModel(Enum):

    """
    Ticket status types with relative identifier.
    """

    CREATED = 'created'

    OPEN = 'open'

    CLOSED = 'closed'
