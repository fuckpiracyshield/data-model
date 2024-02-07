from piracyshield_component.validation.rules.required import Required
from piracyshield_component.validation.rules.string import String
from piracyshield_component.validation.rules.length import Length
from piracyshield_component.validation.rules.fqdn import FQDN
from piracyshield_component.validation.rules.ipv4 import IPv4
from piracyshield_component.validation.rules.ipv6 import IPv6

class TicketRule:

    """
    Set of rules for new ticket.
    """

    TICKET_ID = [
        Required(),
        String(),
        Length(minimum = 32, maximum = 32)
    ]

    DESCRIPTION = [
        Required(),
        String(' .,-_@/\'"'),
        Length(minimum = 3, maximum = 255)
    ]

    FQDN = [
        Required(),
        FQDN()
    ]

    IPV4 = [
        Required(),
        IPv4()
    ]

    IPV6 = [
        Required(),
        IPv6()
    ]
