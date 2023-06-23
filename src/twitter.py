from graphviz import Digraph

dot = Digraph(comment='Twitter Class Diagram')

dot.node('Tweet', 'Tweet\n- tweet_id: int\n- content: str\n- timestamp: datetime\n- author: User')
dot.node('User', 'User\n- user_id: int\n- username: str\n- tweets: List[Tweet]')
dot.node('Twitter', 'Twitter\n- users: List[User]')

dot.edge('Tweet', 'User')
dot.edge('User', 'Tweet', dir='back')
dot.edge('User', 'Twitter')
dot.edge('Twitter', 'User', dir='back')

dot.render('twitter_class_diagram', format='png', view=True)