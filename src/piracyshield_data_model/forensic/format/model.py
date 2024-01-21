
class ForensicFormatsModel:

    """
    Forensic archive formats.
    """

    ZIP = 'zip'

    RAR = 'rar'

    def get_formats(self):
        return [attr for attr in dir(self) if attr.isupper()]
