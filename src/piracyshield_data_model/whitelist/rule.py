from piracyshield_component.validation.rules.required import Required
from piracyshield_component.validation.rules.string import String
from piracyshield_component.validation.rules.length import Length
from piracyshield_component.validation.rules.as_code import ASCode
from piracyshield_component.validation.rules.cidr_syntax_ipv4 import CIDRSyntaxIPv4
from piracyshield_component.validation.rules.cidr_syntax_ipv6 import CIDRSyntaxIPv6

class WhitelistRule:

    """
    Set of rules for new whitelist items.
    """

    REGISTRAR = [
        Required(),
        String(allowed = ' -'),
        Length(minimum = 3, maximum = 255)
    ]

    AS_CODE = [
        Required(),
        ASCode()
    ]

    CIDR_IPV4 = [
        Required(),
        CIDRSyntaxIPv4()
    ]

    CIDR_IPV6 = [
        Required(),
        CIDRSyntaxIPv6()
    ]
