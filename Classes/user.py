# Copyright (c) 2023 Amirmohammad Zarif. All rights reserved.
# Department of Engineering, WTIAU
# Object Oriented Design Course
# Prof. Khoshroo

from typing import List

class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email
        self.tweets = []
        self.followers = []
        self.following = []

    def editProfile(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email

    def createTweet(self, tweet):
        self.tweets.append(tweet)

    def deleteTweet(self, tweet):
        self.tweets.remove(tweet)

    def getTweets(self) -> List[Tweet]:
        return self.tweets

    def getFollowers(self) -> List['User']:
        return self.followers

    def getFollowing(self) -> List['User']:
        return self.following






