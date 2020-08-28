from sqlalchemy.orm import Session

from src.app.base.utils import generate

from . import schemas, crud, models
from ..auth.security import get_password_hash
from ..base.service_base import BaseService


class UserService(BaseService):
    model = models.User
    create_schema = schemas.UserCreateInRegistration
    get_schema = schemas.User_G_Pydantic

    async def create_user(self, schema: schemas.UserCreateInRegistration):
        hash_password = get_password_hash(schema.dict().pop("password"))
        return await self.create(
            schemas.UserCreateInRegistration(
                **schema.dict(exclude={"password"}), password=hash_password
            )
        )


user_s = UserService()


def create_social_account(db: Session, profile: schemas.SocialAccount):
    if crud.social_account.exists(db, account_id=profile.account_id):
        account = crud.social_account.get(db, account_id=profile.account_id)
        return account.user
    # TODO add check user exist
    new_user = schemas.UserCreate(
        username=generate.generate_name(profile.account_login),
        email='soc@gmail.com',
        password=generate.generate_pass(),
        first_name=profile.account_name,
        is_active=True,
        avatar=profile.avatar_url
    )

    user = crud.user.create(db, schema=new_user)
    prof = profile.dict(exclude={"avatar_url"})
    crud.social_account.create(db, schema=prof, user_id=user.id)
    return user

