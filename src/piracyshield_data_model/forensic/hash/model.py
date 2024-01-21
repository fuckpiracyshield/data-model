from piracyshield_data_model.base import BaseModel

from piracyshield_component.validation.validator import Validator

from piracyshield_data_model.forensic.status.model import ForensicArchiveStatusModel

from piracyshield_data_model.forensic.hash.rule import ForensicHashRule

class ForensicHashModel(BaseModel):

    """
    Hash data modeling class.

    This is an extension to validate forensic evidences hashes.
    """

    hash_string = None

    hash_type = None

    status = None

    def __init__(self, hash_string: str, hash_type: str):
        """
        Validates the parameters.

        :param hash_string: a valid hash string based on its type.
        :param hash_type: type of the hash.
        """

        self.hash_type = self._validate_type(hash_type)

        self.hash_string = self._validate_string(hash_string, self.hash_type)

        self.status = ForensicArchiveStatusModel.PENDING.value

    def _validate_type(self, hash_type: str) -> str | Exception:
        """
        Validates the hash.

        :param hash_type: type of the hash.
        :return: the same value.
        """

        # dirty hack to get the list of rules
        hash_types = ForensicHashRule().get_hash_types()

        hash_type = hash_type.upper()

        if hash_type not in hash_types:
            raise ForensicHashModelNotSupportedException()

        return hash_type

    def _validate_string(self, hash_string: str, hash_type: str) -> str | Exception:
        """
        Validates the hash string.

        :param hash_string: a valid hash string.
        :param hash_type: type of the hash.
        :return: the same value.
        """

        if not len(hash_string):
            raise ForensicHashModelHashMissingException()

        validator = Validator(hash_string, getattr(ForensicHashRule, hash_type))

        validator.validate()

        if not validator.is_valid():
            raise ForensicHashModelNonValidException(validator.errors)

        return hash_string

class ForensicHashModelStringMissingException(Exception):

    """
    Hash string is missing.
    """

    pass

class ForensicHashModelNotSupportedException(Exception):

    """
    Non supported hash type.
    """

    pass

class ForensicHashModelNonValidException(Exception):

    """
    Non valid hash string.
    """

    pass
