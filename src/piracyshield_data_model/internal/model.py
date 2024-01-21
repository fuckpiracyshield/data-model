from piracyshield_data_model.account.model import AccountModel
from piracyshield_data_model.account.role.model import AccountRoleModel

class InternalModel(AccountModel):

    """
    Internal account data modeling class.
    """

    role = AccountRoleModel.INTERNAL

    def __init__(self, account_id: str, name: str, email: str, password: str, confirm_password: str, is_active: bool):
        """
        Extends the functionality from a general account.
        """

        super().__init__(account_id, name, email, password, confirm_password, self.role, is_active)
