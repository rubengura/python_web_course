from database import Database
from datetime import datetime
import uuid

__author__ = "rgr"


class Post:

    def __init__(self, blog_id, title, content, author, date=datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    #@staticmethod
    #def from_mongo(id):
    #    data = Database.find_one(collection='posts', query={'id'=id})