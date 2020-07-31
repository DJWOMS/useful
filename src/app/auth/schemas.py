from uuid import UUID
from pydantic import BaseModel


class Token(BaseModel):
    """ Схема для токена
    """
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    """ Схема для
    """
    user_id: int = None


class Msg(BaseModel):
    """ Схема для сообщение
    """
    msg: str


class VerificationInDB(BaseModel):
    """ Схема для проверки email при регистрации
    """
    link: UUID
