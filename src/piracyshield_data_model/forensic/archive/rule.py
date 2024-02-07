from piracyshield_component.validation.rules.required import Required
from piracyshield_component.validation.rules.string import String
from piracyshield_component.validation.rules.length import Length

class ForensicArchiveRule:

    """
    Set of rules for forensic archives.
    """

    NAME = [
        Required(),
        String(allowed = ' .-_'),
        Length(minimum = 6, maximum = 320)
    ]
