from cli.command.command_processor import CommandProcessor
from cli import util

from repository.impl.user_repository import UserRepository

from model.user import User

from datetime import date


class InsertProcessor(CommandProcessor):

    def __init__(self, user_repository: UserRepository):
        super().__init__()

        self.user_repository = user_repository

    def process(self) -> None:
        print("Введи данные пользователя которого необходимо добавить.")
        print(" 1. Имя: ", end="")
        name = util.wait_input("[а-яА-Я]{2,16}")
        print(" 2. Дата рождения (YYYY-MM-DD): ", end="")
        date_of_birth = util.wait_input("[0-9]{4}-(0[0-9]|1[0-2])-([0-2][0-9]|3[0-1])")
        user = User(name, date.fromisoformat(date_of_birth))
        print(f"Пользователь к добавлению: {user}")
        print("Данные верны? (Y/N): ", end="")
        confirmation = util.wait_input("([Yy]|[Nn]).*")
        if "y" not in confirmation.lower():
            return
        self.user_repository.create(user)
        print("Пользователь внесён успешно")