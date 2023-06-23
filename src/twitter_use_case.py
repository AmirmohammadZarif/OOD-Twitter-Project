# Copyright (c) 2023 Amirmohammad Zarif. All rights reserved.
# Department of Engineering, WTIAU
# Object Oriented Design Course
# Prof. Khoshroo

from graphviz import Digraph

dot = Digraph(comment='Twitter Use Case Diagram', format='png')
dot.graph_attr['rankdir'] = 'LR'

with dot.subgraph(name='cluster_Twitter_App') as c:
    c.attr(label='Twitter App', style='rounded')
    c.attr(bgcolor='lightgray', color='black', fontcolor='black')
    c.node_attr.update(shape='rectangle')
    c.edge_attr.update(arrowhead='open')

    c.node('User', shape='actor')
    c.node('Admin', shape='actor')

    c.node('View Timeline', shape='ellipse')
    c.node('Follow User', shape='ellipse')
    c.node('Unfollow User', shape='ellipse')
    c.node('Post Tweet', shape='ellipse')
    c.node('Delete Tweet', shape='ellipse')
    c.node('Search Tweet', shape='ellipse')
    c.node('Block User', shape='ellipse')
    c.node('Report Tweet', shape='ellipse')
    c.node('Manage User', shape='ellipse')

    c.edge('User', 'View Timeline', label='include')
    c.edge('User', 'Follow User', label='include')
    c.edge('User', 'Unfollow User', label='include')
    c.edge('User', 'Post Tweet', label='include')
    c.edge('User', 'Delete Tweet', label='include')
    c.edge('User', 'Search Tweet', label='include')
    c.edge('User', 'Block User', label='include')
    c.edge('User', 'Report Tweet', label='include')
    c.edge('Admin', 'Manage User', label='include')
    c.edge('Manage User', 'Follow User', label='extends')
    c.edge('Manage User', 'Unfollow User', label='extends')
    c.edge('Manage User', 'Block User', label='extends')
    c.edge('Manage User', 'Report Tweet', label='extends')

dot.render('twitter_use_case_diagram', view=True)