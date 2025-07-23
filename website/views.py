from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import  login_required, current_user
from . import db
from .models import Workout

views =  Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/workouts', methods=['GET', 'POST'])
@login_required
def workouts():
    if request.method == 'POST':
        title = request.form['title']
        reps = int(request.form['reps'])
        sets = int(request.form['sets'])
        load = request.form['load']

        new_workout = Workout(title=title, reps=reps, sets=sets, load=load, user_id=current_user.id)
        db.session.add(new_workout)
        db.session.commit()

        return redirect(url_for('views.workouts'))

    # Display workouts
    workouts = Workout.query.filter_by(user_id=current_user.id).all()
    return render_template('workouts.html', workouts=workouts)

@views.route('/delete-workout/<int:id>', methods=['POST'])
@login_required
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    if workout.user_id != current_user.id:
        return "Unauthorized", 403
    db.session.delete(workout)
    db.session.commit()
    return redirect(url_for('views.workouts'))


@views.route('/update-workout/<int:id>', methods=['POST'])
@login_required
def update_workout(id):
    workout = Workout.query.get_or_404(id)
    if workout.user_id != current_user.id:
        return "Unauthorized", 403

    workout.title = request.form['title']
    workout.reps = int(request.form['reps'])
    workout.sets = int(request.form['sets'])
    workout.load = request.form['load']
    db.session.commit()
    return redirect(url_for('views.workouts'))




@views.route('/meal')
@login_required
def meal():
    return render_template('meal.html', user=current_user)

@views.route('/weight')
@login_required
def weight():
    return render_template('weight.html', user=current_user)
