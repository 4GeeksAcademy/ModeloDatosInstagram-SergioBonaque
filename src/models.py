from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    # Relación con posts
    posts = db.relationship('Post', backref='author', lazy=True)
    # Relación con comentarios (opcional, pero útil)
    comments = db.relationship('Comment', backref='commenter', lazy=True)

class Post(db.Model):
    id = db.Column(db.BIGINT, primary_key=True)  
    caption = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    comments = db.relationship('Comment', backref='post', lazy=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)



def serialize(self):
    return {
        "id": self.id,
        "email": self.email,
        # do not serialize the password, its a security breach
    }
