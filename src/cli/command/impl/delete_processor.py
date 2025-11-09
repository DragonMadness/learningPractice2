from cli.command.command_processor import CommandProcessor
from cli import util

from repository.impl.user_repository import UserRepository


class DeleteProcessor(CommandProcessor):

    def __init__(self, user_repository: UserRepository):
        super().__init__()

        self.user_repository = user_repository

    def process(self):
        print("Введи идентификатор пользователя которого необходимо удалить")
        print("Идентификатор пользователя: ", end="")
        id = util.wait_input("[0-9]+")
        deleted = self.user_repository.delete(int(id))
        if deleted is None:
            print("Такого пользователя не существует")
        else:
            print(deleted)