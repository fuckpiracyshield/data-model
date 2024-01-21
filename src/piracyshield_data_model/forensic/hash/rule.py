from piracyshield_component.validation.rules.required import Required
from piracyshield_component.validation.rules.string import String
from piracyshield_component.validation.rules.length import Length

class ForensicHashRule:

    """
    Set of rules for hashes.
    """

    SHA256 = [
        Required(),
        String(),
        Length(minimum = 64, maximum = 64)
    ]

    SHA384 = [
        Required(),
        String(),
        Length(minimum = 96, maximum = 96)
    ]

    SHA512 = [
        Required(),
        String(),
        Length(minimum = 128, maximum = 128)
    ]

    BLAKE2B = [
        Required(),
        String(),
        Length(minimum = 128, maximum = 128)    # accept only default digest size
    ]

    BLAKE2S = [
        Required(),
        String(),
        Length(minimum = 128, maximum = 128)    # accept only default digest size
    ]

    def get_hash_types(self):
        return [attr for attr in dir(self) if attr.isupper()]
