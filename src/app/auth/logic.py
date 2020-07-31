import jwt
from jwt import PyJWTError
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette.status import HTTP_403_FORBIDDEN
from src.config import settings
from src.app.base.utils.db import get_db

from src.app.user.models import User
from src.app.user import crud
from src.app.user import schemas

from .jwt import ALGORITHM
from .schemas import TokenPayload, VerificationInDB
from .crud import auth_verify
from .send_email import send_new_account_email

password_reset_jwt_subject = "preset"
reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


def get_current_user(db: Session = Depends(get_db), token: str = Security(reusable_oauth2)):
    """
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    user = crud.user.get(db, id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(current_user: User = Security(get_current_user)):
    """Проверка активный юзер или нет"""
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(current_user: User = Security(get_current_user)):
    """Проверка суперюзер или нет"""
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user


def registration_user(new_user: schemas.UserCreateInRegistration, db: Session):
    """Регистрация пользователя"""
    if crud.user.get_by_username_email(db, username=new_user.username, email=new_user.email):
        return True
    else:
        user = crud.user.create(db, obj_in=new_user)
        verify = auth_verify.create(db, user.id)
        send_new_account_email(new_user.email, new_user.username, new_user.password, verify.link)
        return False


def verify_registration_user(uuid: VerificationInDB, db: Session):
    """Подтверждение email пользователя"""
    verify = auth_verify.get(db, uuid.link)
    if verify:
        user = crud.user.get(db, verify.user_id)
        crud.user.update(db, db_obj=user, obj_in=schemas.UserUpdate(**{"is_active": "true"}))
        auth_verify.remove(db, uuid.link)
        return True
    else:
        return False


def generate_password_reset_token(email):
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": password_reset_jwt_subject, "email": email},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        assert decoded_token["sub"] == password_reset_jwt_subject
        return decoded_token["email"]
    except InvalidTokenError:
        return None
