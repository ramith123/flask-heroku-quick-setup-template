from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    artist = db.Column(db.String(128), nullable=False)
    album = db.Column(db.String(128), nullable=False)
    albumImgUrl = db.Column(db.String(512), nullable=False, unique=True)
    url = db.Column(db.String(512), nullable=False, unique=True)
    youtubeUrl = db.Column(db.String(512), nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "albumImgUrl": self.albumImgUrl,
            "url": self.url,
            "youtubeUrl": self.youtubeUrl,
        }
