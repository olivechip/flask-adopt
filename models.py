from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

default_photo = "https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small/default-avatar-profile-icon-of-social-media-user-vector.jpg"

class Pet(db.Model):
    """Pet."""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    species = db.Column(db.String, nullable = False)
    photo_url = db.Column(db.String, nullable = True, default = default_photo)
    age = db.Column(db.String, nullable = True)
    notes = db.Column(db.Text, nullable = True)
    available = db.Column(db.Boolean, nullable = False, default = True)