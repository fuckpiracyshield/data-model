from enum import Enum

class ForensicArchiveStatusModel(Enum):

    """
    Forensic archive analysis status.
    """

    PENDING = 'pending'

    SCHEDULED = 'scheduled'

    IN_PROGRESS = 'in progress'

    APPROVED = 'approved'

    REJECTED = 'rejected'
