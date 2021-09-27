from flask_admin.contrib.sqla.view import ModelView
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

#callback function to retrieve a user when a unique identifier is passed 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    passcode = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    blog = db.relationship('NewBlog', backref = 'user', lazy = 'dynamic')


    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.passcode = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.passcode, password)

    def is_active(self):
        return self.active

    def __repr__(self):
        return f'User {self.username}'


#api endpoint class

class Quote_Body:

    randomQuote = []

    def __init__(self, quote, author, permalink):
        self.quote = quote
        self.author = author
        self.permalink = permalink

# Role

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'
 
 # new blog
class NewBlog(db.Model):
    __tablename__ = "blog"

    id = db.Column(db.Integer, primary_key = True)
    blogtitle = db.Column(db.String(255))
    myblog = db.Column(db.String)
    postdate = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.Column(db.String(255))
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    votes = db.relationship('Vote', backref = 'newblog', lazy = 'dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls, id):
        userblogs = NewBlog.query.filter_by(blog_id=id).all()
        return userblogs

class Vote(db.Model):
    __tablename__ = "votes"

    id = db.Column(db.Integer, primary_key = True)
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"))

    def __repr__(self):
        return f'User {self.id}'


