
class BaseModel:

    """
    Base data modeling class with utilities.
    """

    def to_dict(self) -> dict:
        """
        Exports the set data into a dictionary.
        """

        output = {}

        for key, value in self.__dict__.items():
            if value is not None:
                output[key] = value

        return output
