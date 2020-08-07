from typing import Optional
from sqlalchemy.orm import Session
from src.app.auth.security import verify_password, get_password_hash
from src.app.base.crud_base import CRUDBase

from .models import User
from .schemas import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    """ CRUD for user
    """
    def get_by_email(self, db_session: Session, *, email: str) -> Optional[User]:
        return db_session.query(self.model).filter(self.model.email == email).first()

    def get_by_username(self, db_session: Session, *, username: str) -> Optional[User]:
        return db_session.query(self.model).filter(self.model.username == username).first()

    def get_by_username_email(
            self, db_session: Session, *, username: str, email: str
    ) -> Optional[User]:
        return self.exists(db_session, username=username, email=email)

    def create(self, db_session: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            username=obj_in.username,
            email=obj_in.email,
            password=get_password_hash(obj_in.password),
            first_name=obj_in.first_name,
            # is_superuser=obj_in.is_superuser,
        )
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def authenticate(
        self, db_session: Session, *, username: str, password: str
    ) -> Optional[User]:
        user = self.get_by_username(db_session, username=username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser(User)
