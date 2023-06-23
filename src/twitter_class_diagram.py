from graphviz import Digraph

dot = Digraph(comment='Twitter Class Diagram', format='png')
dot.graph_attr['rankdir'] = 'LR'

with dot.subgraph(name='cluster_TwitterApp') as c:
    c.attr(label='TwitterApp', style='rounded')
    c.attr(bgcolor='lightgray', color='black', fontcolor='black')
    c.node_attr.update(shape='record')
    c.edge_attr.update(arrowhead='open')

    c.node('Twitter', r'{class Twitter | -tweets: List<Tweet> | -users: List<User> | '
                      r'+addTweet(tweet: Tweet): void | +deleteTweet(tweet: Tweet): void | '
                      r'+searchTweets(keyword: String): List<Tweet> | +followUser(user: User): void | '
                      r'+unfollowUser(user: User): void}')
    c.node('User', r'{class User | -username: String | -password: String | -email: String | '
                   r'-tweets: List<Tweet> | -followers: List<User> | -following: List<User> | '
                   r'+editProfile(username: String, password: String, email: String): void | '
                   r'+createTweet(tweet: Tweet): void | +deleteTweet(tweet: Tweet): void | '
                   r'+getTweets(): List<Tweet> | +getFollowers(): List<User> | +getFollowing(): List<User>}')
    c.node('Tweet', r'{class Tweet | -id: int | -text: String | -date: Date | -user: User | '
                    r'+getText(): String | +getDate(): Date | +getUser(): User}')
    c.node('UserService', r'{class UserService | +registerUser(username: String, password: String, email: String): User | '
                          r'+loginUser(username: String, password: String): boolean | +logoutUser(): void | '
                          r'+getUserById(id: int): User | +getUserByUsername(username: String): User}')
    c.node('TweetService', r'{class TweetService | +createTweet(text: String, user: User): Tweet | '
                           r'+deleteTweet(tweet: Tweet): void | +getTweetById(id: int): Tweet | '
                           r'+searchTweets(keyword: String): List<Tweet>}')
    c.node('FollowService', r'{class FollowService | +followUser(follower: User, following: User): void | '
                            r'+unfollowUser(follower: User, following: User): void | '
                            r'+getFollowers(user: User): List<User> | +getFollowing(user: User): List<User>}')
    c.node('NotificationService', r'{class NotificationService | +sendNotification(user: User, message: String): void}')

    c.edge('Twitter', 'User')
    c.edge('User', 'Tweet')
    c.edge('User', 'UserService')
    c.edge('Tweet', 'TweetService')
    c.edge('User', 'FollowService')
    c.edge('FollowService', 'User', arrowhead='crow')
    c.edge('NotificationService', 'User', arrowhead='crow')

dot.render('twitter_class_diagram', view=True)