# Copyright (c) 2023 Amirmohammad Zarif. All rights reserved.
# Department of Engineering, WTIAU
# Object Oriented Design Course
# Prof. Khoshroo

from user import User

class UserService:
    def __init__(self):
        self.users = []

    def registerUser(self, username: str, password: str, email: str) -> User:
        user = User(username, password, email)
        self.users.append(user)
        return user

    def loginUser(self, username: str, password: str) -> bool:
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

    def logoutUser(self):
        pass

    def getUserById(self, id: int) -> User:
        for user in self.users:
            if id == user.id:
                return user

    def getUserByUsername(self, username: str) -> User:
        for user in self.users:
            if username == user.username:
                return user
