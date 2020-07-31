from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: Optional[str] = None


class UserBaseInDB(UserBase):
    id: int = None
    username: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

    class Config:
        orm_mode = True


class UserCreate(UserBaseInDB):
    """ Свойства для получения через API при создании из админки
    """
    username: str
    email: str
    password: str
    first_name: str


class UserCreateInRegistration(BaseModel):
    """ Свойства для получения через API при регистрации
    """
    username: str
    email: str
    password: str
    first_name: str

    class Config:
        orm_mode = True


class UserUpdate(UserBaseInDB):
    """ Properties to receive via API on update
    """
    password: Optional[str] = None


class User(UserBaseInDB):
    """ Additional properties to return via API
    """
    pass


class UserInDB(UserBaseInDB):
    """ Additional properties stored in DB
    """
    password: str


class UserPublic(UserBase):
    """ For public profile user
    """
    id: int

    class Config:
        orm_mode = True
