from sqlalchemy.orm import Session
from .models import Verification


class CRUDVerify:
    """ Создание и удаление ссылок подтверждения
    """
    def get(self, db_session: Session, uuid: str) -> Verification:
        return db_session.query(Verification).filter(Verification.link == uuid).first()

    def create(self, db_session: Session, user: int) -> Verification:
        db_obj = Verification(user_id=user)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def remove(self, db_session: Session, uuid: str) -> Verification:
        obj = db_session.query(Verification).filter(Verification.link == uuid).first()
        db_session.delete(obj)
        db_session.commit()
        return obj


auth_verify = CRUDVerify()
