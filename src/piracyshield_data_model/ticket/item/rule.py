from piracyshield_component.validation.rules.required import Required
from piracyshield_component.validation.rules.string import String
from piracyshield_component.validation.rules.length import Length
from piracyshield_component.validation.rules.fqdn import FQDN
from piracyshield_component.validation.rules.ipv4 import IPv4

class TicketItemRule:

    """
    Set of rules for new ticket item.
    """

    TICKET_ITEM_ID = [
        Required(),
        String(),
        Length(minimum = 32, maximum = 32)
    ]
