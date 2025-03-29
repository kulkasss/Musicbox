from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    songs = db.relationship("Song", back_populates="artist")

    def __repr__(self):
        return f"<Artist {self.name}>"


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    artist = db.relationship("Artist", back_populates="songs", lazy="joined")
    title = db.Column(db.String(200), nullable=False)
    file = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Song {self.title}>"


# Модель користувача для авторизації
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(
        db.String(256), nullable=False
    )  # Тут має бути хеш пароля

    def __repr__(self):
        return f"<User {self.username}>"
