import re


def wait_input(*filters: str) -> str:
    patterns: list[re.Pattern] = [re.compile(filter) for filter in filters]
    while True:
        raw: str = input()
        if len(patterns) == 0 or any([pattern.fullmatch(raw) != None for pattern in patterns]):
            return raw
        else:
            print("Некорректный ввод!")