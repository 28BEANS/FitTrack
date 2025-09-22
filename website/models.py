from . import db
from flask_login import UserMixin
from datetime import date

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    birth_day = db.Column(db.String(25))
    routines = db.relationship('Routine', backref='user', lazy=True)
    days = db.relationship('Day', backref='user', lazy=True)

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    label = db.Column(db.String(150), nullable=False)
    workouts = db.relationship('Workout', backref='routine', lazy=True, cascade="all, delete")

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'), nullable=False) 
    title = db.Column(db.String(150), nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    load = db.Column(db.String(100), nullable=False)


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    label = db.Column(db.String(150), nullable=False)
    meals = db.relationship('Meal', backref='day', lazy=True, cascade="all, delete")
    

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'), nullable=False) 
    category = db.Column(db.String(150), nullable=False) 
    name = db.Column(db.String(150), nullable=False)
    serving_size = db.Column(db.String(150), nullable=False)


class WeightEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today) 
    weight = db.Column(db.Float, nullable=False)




