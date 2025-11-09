from cli.command.command_processor import CommandProcessor
from cli import util

from repository.impl.user_repository import UserRepository


class ShowProcessor(CommandProcessor):

    def __init__(self, user_repository: UserRepository):
        super().__init__()

        self.user_repository = user_repository

    def process(self):
        print("Введи идентификатор нужного пользователя или оставь пустым если нужно получить всех")
        print("Идентификатор пользователя: ", end="")
        id = util.wait_input("[0-9]*")
        if len(id) == 0:
            id = "-1"
        users = self.user_repository.read(int(id))
        for user in users:
            print(f" - {user}")
        print(f"Всего записей: {len(users)}")