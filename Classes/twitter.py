# Copyright (c) 2023 Amirmohammad Zarif. All rights reserved.
# Department of Engineering, WTIAU
# Object Oriented Design Course
# Prof. Khoshroo

from user_service import UserService
from tweet_service import TweetService
from follow_service import FollowService
from notification_service import NotificationService
from tweet import Tweet
from typing import List
from user import User

class Twitter:
    def __init__(self):
        self.tweets = []
        self.users = []
        self.userService = UserService()
        self.tweetService = TweetService()
        self.followService = FollowService()
        self.notificationService = NotificationService()

    def addTweet(self, tweet: Tweet):
        self.tweets.append(tweet)

    def deleteTweet(self, tweet: Tweet):
        self.tweets.remove(tweet)

    def searchTweets(self, keyword: str) -> List[Tweet]:
        result = []
        for tweet in self.tweets:
            if keyword in tweet.text:
                result.append(tweet)
        return result

    def followUser(self, user: User):
        self.followService.followUser(self.currentUser, user)

    def unfollowUser(self, user: User):
        self.followService.unfollowUser(self.currentUser, user)