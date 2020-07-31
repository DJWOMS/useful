from src.config import settings
from src.db.session import db_session
from src.app.user.crud import user
from src.app.user.schemas import UserCreate


def main():
    """ Создание супер юзера """
    super_user = user.get_by_username(db_session, username=settings.SUPERUSER_NAME)
    if not super_user:
        user_in = UserCreate(
            username=settings.SUPERUSER_NAME,
            email=settings.SUPERUSER_EMAIL,
            password=settings.SUPERUSER_PASSWORD,
            first_name=settings.SUPERUSER_FIRST_NAME,
            is_superuser=True,
            is_active=True
        )
        user.create(db_session, obj_in=user_in)


main()
