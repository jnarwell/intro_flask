from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint
from flask_login import UserMixin

# DDL Statement
# CREATE TABLE user(
#   id SERIAL PRIMARY KEY,
#   first_name VARCHAR(50) NOT NULL,
# )
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(75), nullable=False, unique=True)
    username = db.Column(db.String(75), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password'))

    def __repr__(self):
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)

@login.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

def random_photo():
    return f"https://picsum.photos/500?random={randint(1,100)}"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False, default=random_photo)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # SQL - FOREIGN KEY(user_id) REFERENCES user(id)

    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'image_url': self.image_url,
            'date_created': self.date_created,
            'user_id': self.user_id
        }
