from piracyshield_component.validation.rules.required import Required
from piracyshield_component.validation.rules.string import String
from piracyshield_component.validation.rules.length import Length

class TicketItemProcessedRule:

    """
    Set of rules for processed ticket item status.
    """

    NOTE = [
        Required(),
        String(' .,-&/$€@"'),
        Length(minimum = 3, maximum = 512)
    ]
