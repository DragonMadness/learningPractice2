from cli import util
from cli.command.impl.show_processor import ShowProcessor
from cli.command.impl.insert_processor import InsertProcessor
from cli.command.impl.delete_processor import DeleteProcessor
from repository.impl.user_repository import UserRepository

USER_REPOSITORY = UserRepository()
COMMANDS={
    "SHOW": ShowProcessor(USER_REPOSITORY),
    "INSERT": InsertProcessor(USER_REPOSITORY),
    "DELETE": DeleteProcessor(USER_REPOSITORY),
    "EXIT": None
}

def main_loop():
    print(
        "Привет! Я помогу тебе взаимодействовать с файловым хранилищем пользователей.\n" \
        "Введи команду из следующего списка:"
    )
    while True:
        for command in COMMANDS:
            print(f" - {command}")
        
        command: str = util.wait_input(
            f"({'|'.join(COMMANDS.keys())})"
        )
        if command == "EXIT":
            return
        COMMANDS[command].process()


if __name__ == '__main__':
    main_loop()