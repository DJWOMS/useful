from typing import List

from fastapi import APIRouter, Depends, Body, Form

from src.app.auth.permissions import get_user

from src.app.user import models, schemas, service


user_router = APIRouter()


@user_router.get('/me', response_model=schemas.UserPublic)
def user_me(current_user: models.User = Depends(get_user)):
    """ Get current user """
    if current_user:
        return current_user

