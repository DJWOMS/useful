from fastapi import BackgroundTasks

from fastapi import APIRouter, Body, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm

from src.config.social_app import social_auth, redirect_uri

from src.app.user import service, schemas

from .schemas import Token, Msg, VerificationOut
from .jwt import create_token
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
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """ OAuth2 compatible token login, get an access token for future requests
    """
    user = await service.user_s.authenticate(username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return create_token(user.id)


@auth_router.post("/registration", response_model=Msg)
async def user_registration(new_user: schemas.UserCreateInRegistration, task: BackgroundTasks):
    """ Регистрация пользователя
    """
    user = await registration_user(new_user, task)
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    else:
        return {"msg": "Send email"}


@auth_router.post("/confirm-email", response_model=Msg)
async def confirm_email(uuid: VerificationOut):
    if await verify_registration_user(uuid):
        return {"msg": "Success verify email"}
    else:
        raise HTTPException(status_code=404, detail="Not found")


@auth_router.post("/password-recovery/{email}", response_model=Msg)
async def recover_password(email: str, task: BackgroundTasks):
    """ Password Recovery
    """
    user = await service.user_s.get_obj(email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    password_reset_token = generate_password_reset_token(email)
    task.add_task(
        send_reset_password_email, email_to=user.email, email=email, token=password_reset_token
    )
    return {"msg": "Password recovery email sent"}


@auth_router.post("/reset-password/", response_model=Msg)
async def reset_password(token: str = Body(...), new_password: str = Body(...)):
    """ Reset password
    """
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = await service.user_s.get_obj(email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    await service.user_s.change_password(user, new_password)
    return {"msg": "Password updated successfully"}


@auth_router.get('/')
async def login_oauth(request: Request):
    github = social_auth.create_client('github')
    return await github.authorize_redirect(request, redirect_uri)


@auth_router.get('/github_login', response_model=schemas.SocialAccountGet)
async def authorize(request: Request):
    # TODO I need add check profile exists
    token = await social_auth.github.authorize_access_token(request)
    resp = await social_auth.github.get('user', token=token)
    profile = resp.json()
    return schemas.SocialAccountGet(
        account_id=profile.get("id"),
        account_url=profile.get("html_url"),
        account_login=profile.get("login"),
        account_name=profile.get("name"),
        avatar_url=profile.get("avatar_url"),
        provider="github"
    )


@auth_router.post('/create_oauth')
async def create_oauth(profile: schemas.SocialAccount):
    user = await service.social_account_s.create_social_account(profile)
    return create_token(user.id)
