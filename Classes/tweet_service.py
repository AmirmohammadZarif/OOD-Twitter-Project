# Copyright (c) 2023 Amirmohammad Zarif. All rights reserved.
# Department of Engineering, WTIAU
# Object Oriented Design Course
# Prof. Khoshroo

from tweet import Tweet

class TweetService:
    def __init__(self):
        self.tweets = []

    def createTweet(self, text: str, user: User) -> Tweet:
        tweet = Tweet(len(self.tweets), text, 'now', user)
        self.tweets.append(tweet)
        return tweet

    def deleteTweet(self, tweet: Tweet):
        self.tweets.remove(tweet)

    def getTweetById(self, id: int) -> Tweet:
        for tweet in self.tweets:
            if id == tweet.id:
                return tweet

    def searchTweets(self, keyword: str) -> List[Tweet]:
        result = []
        for tweet in self.tweets:
            if keyword in tweet.text:
                result.append(tweet)
        return result