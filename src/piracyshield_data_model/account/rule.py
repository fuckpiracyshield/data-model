from piracyshield_component.validation.rules.required import Required
from piracyshield_component.validation.rules.string import String
from piracyshield_component.validation.rules.length import Length
from piracyshield_component.validation.rules.email import Email

class AccountRule:

    """
    Set of rules for new account generation.
    """

    ACCOUNT_ID = [
        Required(),
        String(),
        Length(minimum = 32, maximum = 32)
    ]

    NAME = [
        Required(),
        String(allowed = ' _-.'),
        Length(minimum = 3, maximum = 255)
    ]

    EMAIL = [
        Required(),
        String(allowed = '@._-'),
        Email()
    ]

    PASSWORD = [
        Required(),
        String(allowed = '-_%~&@'),
        Length(minimum = 8, maximum = 32)
    ]

    ROLE = [
        Required(),
        Length(minimum = 3, maximum = 3)
    ]
