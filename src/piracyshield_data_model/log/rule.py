from piracyshield_component.validation.rules.required import Required
from piracyshield_component.validation.rules.string import String
from piracyshield_component.validation.rules.length import Length

class LogRule:

    """
    Set of rules for log records.
    """

    LOG_ID = [
        Required(),
        String(),
        Length(minimum = 32, maximum = 32)
    ]

    MESSAGE = [
        Required(),
        Length(minimum = 3, maximum = 500)
    ]
