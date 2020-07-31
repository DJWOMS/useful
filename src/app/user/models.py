from sqlalchemy import Column, String, Integer, DateTime, Boolean, sql
from src.db.session import Base


class User(Base):
    __tablename__ = "user_user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String(150))
    last_name = Column(String(150))
    date_join = Column(DateTime(timezone=True), server_default=sql.func.now())
    last_login = Column(DateTime)
    is_active = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    avatar = Column(String)

