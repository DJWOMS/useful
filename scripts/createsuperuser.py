import typer
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.db.session import db_session
from src.app.user.crud import user
from src.app.user.schemas import UserCreate


def main():
    """ Создание супер юзера
    """
    typer.echo("Create superuser")
    name = typer.prompt("Username")
    email = typer.prompt("Email")
    first_name = typer.prompt("First name")
    password = typer.prompt("Password")
    super_user = user.get_by_username_email(db_session, username=name, email=email)
    if not super_user:
        user_in = UserCreate(
            username=name,
            email=email,
            password=password,
            first_name=first_name,
            is_superuser=True,
            is_active=True
        )
        user.create_superuser(db_session, schema=user_in)
        mess = typer.style("Success", fg=typer.colors.GREEN)
    else:
        mess = typer.style("Error, user existing", fg=typer.colors.RED)
    typer.echo(mess)


if __name__ == '__main__':
    typer.run(main)
