"""
Observer Design Patter
"""

class User:
    '''
    User class will act role of observer to subject
    '''
    def __init__(self, name):
        self.name = name

    def update(self, article, blog_writer):
        print(f'For {article}, new article by {blog_writer} is added')