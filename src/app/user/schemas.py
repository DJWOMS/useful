from typing import Optional

from fastapi import Body, Form
from pydantic import BaseModel, EmailStr
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import User


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
    email: EmailStr
    password: str
    first_name: str
    avatar: str = None


class UserCreateInRegistration(BaseModel):
    """ Свойства для получения через API при регистрации
    """
    username: str
    email: EmailStr
    password: str
    first_name: str
    avatar: str = None

    class Config:
        orm_mode = True


class UserUpdate(UserBaseInDB):
    """ Properties to receive via API on update
    """
    password: Optional[str] = Form(...)


# class User(UserBaseInDB):
#     """ Additional properties to return via API
#     """
#     pass


class UserInDB(UserBaseInDB):
    """ Additional properties stored in DB
    """
    password: str


class SocialAccount(BaseModel):
    """ Schema social accounts
    """
    account_id: int
    account_url: str
    account_login: str
    account_name: str
    provider: str
    user: UserCreateInRegistration

    class Config:
        orm_mode = True


class SocialAccountGet(BaseModel):
    """ Schema social accounts
    """
    account_id: int
    account_url: str
    account_login: str
    account_name: str
    provider: str
    avatar_url: str

    class Config:
        orm_mode = True


class UserPublic(UserBase):
    """ For public profile user
    """
    id: int
    # social_account: SocialAccount

    class Config:
        orm_mode = True


User_C_Pydantic = pydantic_model_creator(
    User, name='create_user', exclude_readonly=True, exclude=('is_active', 'is_staff', 'is_superuser'))
User_G_Pydantic = pydantic_model_creator(User, name='user')
