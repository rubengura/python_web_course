__author__ = "rgr"

from database import Database
from models.post import Post


Database.initialize()

post = Post(blog_id='123',
            title='A post',
            content="Some content for the post",
            author='Rubén')

post.save_to_mongo()