from .models import Verification
from .schemas import VerificationOut, VerificationCreate
from ..base.crud_base import CRUDBase


class VerifyCRUD(CRUDBase[Verification, VerificationCreate, VerificationOut]):
    """ Создание и удаление ссылок подтверждения
    """
    pass


auth_verify = VerifyCRUD(Verification)
