from enum import Enum

class TicketItemStatusModel(Enum):

    """
    Ticket item status types with relative identifier.
    """

    PENDING = 'pending'

    PROCESSED = 'processed'

    UNPROCESSED = 'unprocessed'

    UNBLOCKED = 'unblocked'
