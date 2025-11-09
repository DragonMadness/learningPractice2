from abc import abstractmethod, ABC


class CommandProcessor(ABC):
    @abstractmethod
    def process(self) -> None:
        pass