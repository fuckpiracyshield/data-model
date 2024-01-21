from enum import IntEnum

class AccountRoleModel(IntEnum):

    """
    Account types with relative identifier.
    """

    GUEST = 100

    INTERNAL = 200

    REPORTER = 300

    PROVIDER = 400
