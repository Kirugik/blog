import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    def setUp(self):
        self.new_user = User(email="robertkirui@mail.com", username ="robert", password="robertkirui")
        self.new_post = Post(title = "new blog post", text="This is my new blog post", author=self.new_user.id)
        self.new_comment = Comment(text="I like it", post_id=self.new_post.id, author=self.new_user.id) 

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))


        