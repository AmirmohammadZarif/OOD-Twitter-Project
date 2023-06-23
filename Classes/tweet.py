# Copyright (c) 2023 Amirmohammad Zarif. All rights reserved.
# Department of Engineering, WTIAU
# Object Oriented Design Course
# Prof. Khoshroo

from user import User

class Tweet:
    def __init__(self, id: int, text: str, date: str, user: User):
        self.id = id
        self.text = text
        self.date = date
        self.user = user

    def getText(self) -> str:
        return self.text

    def getDate(self) -> str:
        return self.date

    def getUser(self) -> User:
        return self.user
