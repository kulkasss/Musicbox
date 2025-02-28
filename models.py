from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    songs = db.Relationships('Song', backref='artist', lazy=True, cascade = "all, delete")

    def __repr__(self):
        return f"<Artist {self.name}>"


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    file = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Song {self.title}>"
