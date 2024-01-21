from enum import IntEnum

class PermissionModel(IntEnum):

    """
    Permission types with relative identifier.
    """

    # account permissions

    CREATE_ACCOUNT = 101

    VIEW_ACCOUNT = 102

    EDIT_ACCOUNT = 103

    DELETE_ACCOUNT = 104

    # ticket permissions

    CREATE_TICKET = 201

    VIEW_TICKET = 202

    EDIT_TICKET = 203

    DELETE_TICKET = 204

    UPLOAD_TICKET = 205

    # whitelist permissions

    CREATE_WHITELIST_ITEM = 301

    VIEW_WHITELIST_ITEM = 302

    EDIT_WHITELIST_ITEM = 303

    DELETE_WHITELIST_ITEM = 304

    # DDA permissions

    CREATE_DDA = 401

    VIEW_DDA = 402

    EDIT_DDA = 403

    DELETE_DDA = 404
