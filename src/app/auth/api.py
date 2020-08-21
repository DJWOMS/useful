from datetime import timedelta

from fastapi import APIRouter, Body, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from starlette.responses import JSONResponse

from src.config import settings
from src.config.social_app import social_auth
from src.app.base.utils.db import get_db

from src.app.user import service, crud, schemas

from .schemas import Token, Msg, VerificationOut
from .permissions import get_current_user
from .jwt import create_access_token
from .security import get_password_hash
from .send_email import send_reset_password_email
from .service import (
    generate_password_reset_token,
    verify_password_reset_token,
    registration_user,
    verify_registration_user
)


auth_router = APIRouter()


@auth_router.post("/login/access-token", response_model=Token)
def login_access_token(
        db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
    ):
    """ OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(
        db, username=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            data={"user_id": user.id}, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@auth_router.post("/registration", response_model=Msg)
def user_registration(new_user: schemas.UserCreateInRegistration, db: Session = Depends(get_db)):
    """ Регистрация пользователя
    """
    user = registration_user(new_user, db)
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    else:
        return {"msg": "Send email"}


@auth_router.post("/confirm-email", response_model=Msg)
def confirm_email(uuid: VerificationOut, db: Session = Depends(get_db)):
    if verify_registration_user(uuid, db):
        return {"msg": "Success verify email"}
    else:
        raise HTTPException(status_code=404, detail="Not found")


@auth_router.post("/password-recovery/{email}", response_model=Msg)
def recover_password(email: str, db: Session = Depends(get_db)):
    """ Password Recovery
    """
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    password_reset_token = generate_password_reset_token(email)
    send_reset_password_email(email_to=user.email, email=email, token=password_reset_token)
    return {"msg": "Password recovery email sent"}


@auth_router.post("/reset-password/", response_model=Msg)
def reset_password(
        token: str = Body(...), new_password: str = Body(...), db: Session = Depends(get_db)
    ):
    """ Reset password
    """
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    hashed_password = get_password_hash(new_password)
    crud.user.change_password(db, user, hashed_password)
    return {"msg": "Password updated successfully"}


@auth_router.get('/')
async def login(request: Request):
    github = social_auth.create_client('github')
    redirect_uri = 'http://localhost:8000/api/v1/auth/github_login'
    return await github.authorize_redirect(request, redirect_uri)


@auth_router.get('/github_login')
async def authorize(request: Request, db: Session = Depends(get_db)):
    token = await social_auth.github.authorize_access_token(request)
    resp = await social_auth.github.get('user', token=token)
    profile = resp.json()
    prof = schemas.SocialAccount(
        account_id=profile.get("id"),
        account_url=profile.get("html_url"),
        account_login=profile.get("login"),
        account_name=profile.get("name"),
        avatar_url=profile.get("avatar_url"),
        provider="github"
    )
    user = service.create_social_account(db, prof)
    # TODO add new function, return {token}
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            data={"user_id": user.id}, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
