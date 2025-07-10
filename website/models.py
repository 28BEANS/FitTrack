from . import db
from flask_login import UserMixin

class User(db.model, UserMixin):
    id  = db.Column(db.Integer, primay_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))