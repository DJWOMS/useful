from fastapi import APIRouter, Depends

from src.app.auth.permissions import get_active_user

from src.app.user import models, schemas


user_router = APIRouter()


@user_router.get('/me', response_model=schemas.UserPublic)
def user_me(current_user: models.User = Depends(get_active_user)):
    if current_user:
        return current_user
