# Copyright (c) 2023 Amirmohammad Zarif. All rights reserved.
# Department of Engineering, WTIAU
# Object Oriented Design Course
# Prof. Khoshroo

from user import User
from typing import List


class FollowService:
    def followUser(self, follower: User, following: User):
        follower.following.append(following)
        following.followers.append(follower)

    def unfollowUser(self, follower: User, following: User):
        follower.following.remove(following)
        following.followers.remove(follower)

    def getFollowers(self, user: User) -> List[User]:
        return user.followers

    def getFollowing(self, user: User) -> List[User]:
        return user.following