from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    files = db.relationship('Music', backref='task', lazy=True, cascade="all, delete")

    def __repr__(self):
        return f"<Music {self.title}>"
class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    music_id = db.Column(db.Integer, db.ForeignKey('music_id.id'), nullable=False)