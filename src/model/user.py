from datetime import date

class User:
    def __init__(self, name: str, date_of_birth: date, id: int=-1):
        self.id: int = id
        self.name: str = name
        self.date_of_birth: date = date_of_birth

    def __str__(self) -> str:
        return f"User({self.id}; {self.name}; {self.date_of_birth.isoformat()})"

    def serialize(self: User) -> dict[str, str]:
        return {
            "id": str(self.id),
            "name": self.name,
            "date_of_birth": self.date_of_birth.isoformat()
        }

    @staticmethod
    def deserialize(data: dict[str, str]) -> User:
        return User(data["name"], date.fromisoformat(data["date_of_birth"]), int(data["id"]))