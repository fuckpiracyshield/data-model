from piracyshield_component.validation.rules.required import Required
from piracyshield_component.validation.rules.string import String
from piracyshield_component.validation.rules.length import Length
from piracyshield_component.validation.rules.dda import DDA

class DDARule:

    """
    Set of rules for a DDA item.
    """

    DDA_ID = [
        Required(),
        String(),
        Length(minimum = 32, maximum = 32)
    ]

    DESCRIPTION = [
        Required(),
        String(' .,-_@'),
        Length(minimum = 3, maximum = 255)
    ]

    INSTANCE = [
        Required(),
        DDA()
    ]
