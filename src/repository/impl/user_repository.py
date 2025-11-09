from repository.base_repository import BaseRepository
from model.user import User


class UserRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__("../data/users.json")

    def create(self, object: User) -> None:
        users = self.read_collection("users")
        if users is None:
            users = []
        if object.id == -1:
            if len(users) == 0:
                object.id = 0
            else:
                object.id = max([int(user["id"]) for user in users]) + 1
        users.append(object.serialize())
        self.write_collection("users", users)
    
    def read(self, id: int=-1) -> list[User]:
        users = self.read_collection("users")
        if users is None:
            return []
        userdata_search = users
        if id != -1:
            userdata_search = [userdata for userdata in users if int(userdata["id"]) == id]
        if len(userdata_search) == 0:
            return []
        return [User.deserialize(userdata) for userdata in userdata_search]
    
    def delete(self, id: int) -> User | None:
        users = self.read_collection("users")
        if users is None:
            return None
        to_remove_search = [userdata for userdata in users if int(userdata["id"]) == id]
        if len(to_remove_search) == 0:
            return None
        users.remove(to_remove_search[0])
        self.write_collection("users", users)
        return User.deserialize(to_remove_search[0])
