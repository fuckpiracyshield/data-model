from enum import Enum

class TicketStatusModel(Enum):

    """
    Ticket status types with relative identifier.
    """

    CREATING = 'creating'

    CREATED = 'created'

    OPEN = 'open'

    CLOSED = 'closed'

    FAILED = 'failed'
