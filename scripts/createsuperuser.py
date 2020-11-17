import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tortoise import Tortoise, run_async
from src.config import settings
from src.app.user.service import user_s
from src.app.user.schemas import UserCreateInRegistration


async def main():
    """ Создание супер юзера
    """
    await Tortoise.init(
        db_url=settings.DATABASE_URI,
        modules={"models": settings.APPS_MODELS},
    )
    print("Create superuser")
    name = input("Username: ")
    email = input("Email: ")
    first_name = input("First name: ")
    password = input("Password: ")
    super_user = await user_s.get_username_email(username=name, email=email)
    if not super_user:
        user_in = UserCreateInRegistration(
            username=name,
            email=email,
            password=password,
            first_name=first_name,
        )
        await user_s.create_superuser(schema=user_in)
        print("Success")
    else:
        print("Error, user existing")


if __name__ == '__main__':
    run_async(main())
