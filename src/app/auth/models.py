from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from src.db.session import Base


class Verification(Base):
    """ Модель для подтверждения регистрации пользователя
    """
    __tablename__ = "auth_verification"

    link = Column(UUID(as_uuid=True), default=uuid4)
    user_id = Column(Integer, ForeignKey("user_user.id"))
