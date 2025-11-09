from abc import ABC, abstractmethod
from typing import Any
import json
import os


class BaseRepository(ABC):
    def __init__(self, file_path: str = "./database.json") -> None:
        super().__init__()
        self.file_path = file_path

        self.ensure_file_exists(file_path)

    @abstractmethod
    def create(self, object: Any) -> None:
        pass

    @abstractmethod
    def read(self, id: int) -> object:
        pass

    @abstractmethod
    def delete(self, id: int) -> object | None:
        pass

    def read_file(self) -> dict[str, Any]:
        with open(self.file_path, encoding="utf-8") as file:
            data = file.read()
        return json.loads(data)
    
    def write_file(self, data: dict[str, Any]) -> None:
        raw = json.dumps(data, ensure_ascii=False)
        with open(self.file_path, mode="w", encoding="utf-8") as file:
            file.write(raw)

    def read_collection(self, name: str) -> list[dict] | None:
        data = self.read_file()
        if name in data.keys():
            return data[name]
        return None

    def write_collection(self, name: str, collection: list[dict]) -> None:
        data = self.read_file()
        data[name] = collection
        self.write_file(data)

    @staticmethod
    def ensure_file_exists(path: str) -> None:
        if os.path.exists(path):
           return
        if "/" in path:
            dirs = "/".join(path.split("/")[:-1:])
            os.makedirs(dirs, exist_ok=True)
        with open(path, mode="w") as file:
            file.write("{}")
