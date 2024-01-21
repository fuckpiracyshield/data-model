from piracyshield_component.validation.rules.required import Required
from piracyshield_component.validation.rules.string import String
from piracyshield_component.validation.rules.length import Length
from piracyshield_component.validation.rules.email import Email

class AuthenticationRule:

    """
    Set of rules for user authentication.
    """

    EMAIL = [
        Required(),
        String('@._-'),
        Email()
    ]

    PASSWORD = [
        Required(),
        String(allowed = '-_%~&@'),
        Length(minimum = 8, maximum = 32)
    ]
