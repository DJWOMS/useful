from fastapi import APIRouter, Depends

from src.app.auth.permissions import get_user

from src.app.user import models, schemas, service


user_router = APIRouter()


@user_router.get('/me', response_model=schemas.UserPublic)
def user_me(current_user: models.User = Depends(get_user)):
    """ Get user
    """
    if current_user:
        return current_user


@user_router.post('/test/create', response_model=schemas.User_G_Pydantic)
async def test_create(user: schemas.UserCreateInRegistration):
    return await service.user_s.create_user(user)


@user_router.post('/test/update', response_model=schemas.User_G_Pydantic)
async def test_create(user: schemas.UserUpdate):
    return await service.user_s.update(user)
