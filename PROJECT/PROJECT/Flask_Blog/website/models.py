from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete="CASCADE"),nullable=False)
    name = db.Column(db.String(1000))
    like = db.Column(db.Integer)

class images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete="CASCADE"))
    image = db.Column(db.BLOB)
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notes = db.relationship('Note', backref='user', passive_deletes=True)
    image = db.relationship('images', backref='user', passive_deletes=True)
    