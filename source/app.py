__author__ = "rgr"

from database import Database
from models.post import Post
from models.blog import Blog


Database.initialize()

post = Post(blog_id='123',
            title='A post',
            content="Some content for the post",
            author='Rubén')

post.save_to_mongo()

blog = Blog(author="Rubén",
            title="Sample title",
            description="Sample description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)
