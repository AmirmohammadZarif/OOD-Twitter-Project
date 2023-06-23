from graphviz import Digraph

dot = Digraph(comment='Twitter Class Diagram', format='png')
dot.graph_attr['rankdir'] = 'LR'

with dot.subgraph(name='cluster_TwitterApp') as c:
    c.attr(label='TwitterApp', style='rounded')
    c.attr(bgcolor='lightgray', color='black', fontcolor='black')
    c.node_attr.update(shape='rectangle', height='0', width='0')
    c.edge_attr.update(arrowhead='open')

    c.node('Twitter', r'class Twitter\l-tweets: List<Tweet>\l-users: List<User>\l+addTweet(tweet: Tweet): void\l+deleteTweet(tweet: Tweet): void\l+searchTweets(keyword: String): List<Tweet>\l+followUser(user: User): void\l+unfollowUser(user: User): void')
    c.node('User', r'class User\l-username: String\l-password: String\l-email: String\l-tweets: List<Tweet>\l-followers: List<User>\l-following: List<User>\l+editProfile(username: String, password: String, email: String): void\l+createTweet(tweet: Tweet): void\l+deleteTweet(tweet: Tweet): void\l+getTweets(): List<Tweet>\l+getFollowers(): List<User>\l+getFollowing(): List<User>')
    c.node('Tweet', r'class Tweet\l-id: int\l-text: String\l-date: Date\l-user: User\l+getText(): String\l+getDate(): Date\l+getUser(): User')
    c.node('UserService', r'class UserService\l+registerUser(username: String, password: String, email: String): User\l+loginUser(username: String, password: String): boolean\l+logoutUser(): void\l+getUserById(id: int): User\l+getUserByUsername(username: String): User')
    c.node('TweetService', r'class TweetService\l+createTweet(text: String, user: User): Tweet\l+deleteTweet(tweet: Tweet): void\l+getTweetById(id: int): Tweet\l+searchTweets(keyword: String): List<Tweet>')
    c.node('FollowService', r'class FollowService\l+followUser(follower: User, following: User): void\l+unfollowUser(follower: User, following: User): void\l+getFollowers(user: User): List<User>\l+getFollowing(user: User): List<User>')
    c.node('NotificationService', r'class NotificationService\l+sendNotification(user: User, message: String): void')

    c.edge('Twitter', 'User')
    c.edge('User', 'Tweet')
    c.edge('User', 'UserService')
    c.edge('Tweet', 'TweetService')
    c.edge('User', 'FollowService')
    c.edge('FollowService', 'User', arrowhead='crow')
    c.edge('NotificationService', 'User', arrowhead='crow')

dot.render('twitter_class_diagram', view=True)