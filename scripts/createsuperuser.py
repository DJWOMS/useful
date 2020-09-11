import typer
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app.user.service import user_s
from src.app.user.schemas import UserCreateInRegistration


def main():
    """ Создание супер юзера
    """
    typer.echo("Create superuser")
    name = typer.prompt("Username")
    email = typer.prompt("Email")
    first_name = typer.prompt("First name")
    password = typer.prompt("Password")
    super_user = user_s.get_obj(username=name, email=email)
    if not super_user:
        user_in = UserCreateInRegistration(
            username=name,
            email=email,
            password=password,
            first_name=first_name,
        )
        user_s.create_superuser(schema=user_in)
        mess = typer.style("Success", fg=typer.colors.GREEN)
    else:
        mess = typer.style("Error, user existing", fg=typer.colors.RED)
    typer.echo(mess)


if __name__ == '__main__':
    typer.run(main)
