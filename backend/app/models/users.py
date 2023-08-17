
from ..extensions import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    passw = db.Column(db.String, unique=True, nullable=False)
