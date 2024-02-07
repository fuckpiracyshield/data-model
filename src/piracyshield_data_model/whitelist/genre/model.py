from enum import Enum

class WhitelistGenreModel(Enum):

    """
    Whitelist item genres.
    """

    FQDN = 'fqdn'

    IPV4 = 'ipv4'

    IPV6 = 'ipv6'

    CIDR_IPV4 = 'cidr_ipv4'

    CIDR_IPV6 = 'cidr_ipv6'
