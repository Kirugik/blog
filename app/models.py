from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash 



# define User database model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True)
    username = db.Column(db.String(255),unique = True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    bio = db.Column(db.String(255)) 
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    likes = db.relationship('Like', backref='user', passive_deletes=True)
    
    
    # @property
    # def password(self):
    #     raise AttributeError("You cannot read the password attribute")
        
    # @password.setter
    # def password(self, password):
    #     self.password = generate_password_hash(password)
    
    # def verify_password(self, password):
    #         return check_password_hash(self.password, password) 



# define Post database model 
class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String, nullable = False) 
    text = db.Column(db.Text, nullable=False) 
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    comments = db.relationship('Comment', backref='post', passive_deletes=True)
    likes = db.relationship('Like', backref='post', passive_deletes=True)
    
    
    # def save_post(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete_post(self):
    #     db.session.delete(self)
    #     db.session.commit()

    # @classmethod
    # def get_all_posts(cls):
    #     return Post.query.order_by(Post.date_created).all()



# define Comment database model 
class Comment(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)
    
    
    # def save_comment(self):
    #     db.session.add(self)
    #     db.session.commit()

    # @classmethod
    # def delete_comment(cls, id):
    #     deleted = Comment.query.filter_by(id = id).first()
    #     db.session.delete(deleted) 
    #     db.session.commit()

    # @classmethod
    # def get_comments(cls,id):
    #     comments = Comment.query.filter_by(post_id = id).all()
    #     return comments 



# define Like database model 
class Like (db.Model):
    id = db.Column(db.Integer,primary_key = True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False) 


class Quote: 
    """
    Blueprint class for quotes consumed from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote 