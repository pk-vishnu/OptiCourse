from . import db 
from flask_login import UserMixin 
from sqlalchemy.sql import func

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course= db.Column(db.String(150))
    credit=db.Column(db.Float)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))

