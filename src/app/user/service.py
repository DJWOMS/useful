from typing import Optional

from src.app.auth.security import verify_password, get_password_hash

from . import schemas, models
from ..base.service_base import BaseService


class UserService(BaseService):
    model = models.User
    create_schema = schemas.UserCreateInRegistration
    get_schema = schemas.User_G_Pydantic

    async def create_user(self, schema: schemas.UserCreateInRegistration, **kwargs):
        hash_password = get_password_hash(schema.dict().pop("password"))
        return await self.create(
            schemas.UserCreateInRegistration(
                **schema.dict(exclude={"password"}), password=hash_password, **kwargs
            )
        )

    async def authenticate(self, username: str, password: str) -> Optional[models.User]:
        user = await self.model.get(username=username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    async def change_password(self, obj: models.User, new_password: str):
        hashed_password = get_password_hash(new_password)
        obj.password = hashed_password
        await obj.save()

    async def create_user_social(self, user: schemas.UserCreateInRegistration):
        return await self.create_user(schema=user, is_active=True)

    def create_superuser(self, user: schemas.UserCreateInRegistration):
        return self.create_user(schema=user, is_active=True, is_superuser=True)


class SocialAccountService(BaseService):
    model = models.SocialAccount
    # create_schema = schemas.UserCreateInRegistration
    # get_schema = schemas.User_G_Pydantic

    async def create_social_account(self, profile: schemas.SocialAccount):
        # TODO fix if user exists, return "QuerySet' object has no attribute 'id"
        account = await self.get_obj(account_id=profile.account_id)
        if account:
            return account.user
        user = await user_s.create_user_social(profile.user)
        if user:
            await self.model.create(**profile.dict(exclude={"user"}), user_id=user.id)
            return user
        else:
            pass


user_s = UserService()
social_account_s = SocialAccountService()
