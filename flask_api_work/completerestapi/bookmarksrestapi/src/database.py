from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    name = db.Column('user_name', db.String(80), unique=True, nullable=False)
    email = db.Column('user_email', db.String(180), unique=True, nullable=False)
    password = db.Column('user_password', db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    bookmarks = db.relationship('Bookmark', backref='user')

    def __str__(self) -> str:
        return f"User>>>{self.name}"


class Bookmark(db.Model):
    __tablename__ = 'bookmarks'
    id = db.Column('bookmark_id', db.Integer, primary_key=True)
    body = db.Column('bookmark_body', db.Text, nullable=True)
    url = db.Column('bookmark_url', db.Text, nullable=False)
    short_url = db.Column('bookmark_shorturl', db.String(3), nullable=True)
    visits = db.Column(db.Integer, default=0)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def generate_short_characters(self):
        charcters=string.digits+string.ascii_letters
        picked_chars=random.choices(charcters,k=3)
        picked_chars=''.join(picked_chars)
        link=self.query.filter_by(short_url=picked_chars).first()

        if link:
            self.generate_short_characters()
        else:
            return picked_chars

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.short_url=self.generate_short_characters()

    def __repr__(self) -> str:
        return "Bookmark>>> {self.url}"