from sqlalchemy import Column, String, DateTime, Boolean, sql, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.db.session import Base


class User(Base):
    __tablename__ = "user_user"

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


class SocialAccount(Base):
    """ Model social accounts
    """
    __tablename__ = "user_social_account"

    account_id = Column(Integer)
    account_url = Column(String)
    account_login = Column(String)
    account_name = Column(String)
    provider = Column(String)

    user_id = Column(Integer, ForeignKey('user_user.id', ondelete='CASCADE'))
    user = relationship("User", backref=backref('social_account'))


