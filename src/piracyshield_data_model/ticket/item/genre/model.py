from enum import Enum

class TicketItemGenreModel(Enum):

    """
    Ticket item genre types with relative identifier.
    """

    FQDN = 'fqdn'

    IPV4 = 'ipv4'

    IPV6 = 'ipv6'
