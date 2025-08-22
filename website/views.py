from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import  login_required, current_user
from . import db
from .models import Workout, Routine, Meal

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
        routine_id = int(request.form['routine_id'])

        routine = Routine.query.filter_by(id=routine_id, user_id=current_user.id).first()
        if not routine:
            return "Invalid routine.", 400

        new_workout = Workout(
            title=title,
            reps=reps,
            sets=sets,
            load=load,
            routine_id=routine_id
        )
        db.session.add(new_workout)
        db.session.commit()

        return redirect(url_for('views.workouts'))

    routines = Routine.query.filter_by(user_id=current_user.id).all()
    workouts_by_routine = {r: r.workouts for r in routines}
    return render_template('workouts.html', routines=routines, workouts_by_routine=workouts_by_routine)

@views.route('/delete-workout/<int:id>', methods=['POST'])
@login_required
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    if workout.routine.user_id != current_user.id:
        return "Unauthorized", 403
    db.session.delete(workout)
    db.session.commit()
    return redirect(url_for('views.workouts'))


@views.route('/update-workout/<int:id>', methods=['POST'])
@login_required
def update_workout(id):
    workout = Workout.query.get_or_404(id)

    # Corrected ownership check via routine
    if workout.routine.user_id != current_user.id:
        return "Unauthorized", 403

    workout.title = request.form['title']
    workout.reps = int(request.form['reps'])
    workout.sets = int(request.form['sets'])
    workout.load = request.form['load']
    db.session.commit()
    return redirect(url_for('views.workouts'))

@views.route('/add-routine', methods=['POST'])
@login_required
def add_routine():
    label = request.form['label']
    if not label.strip():
        return "Routine label required", 400

    new_routine = Routine(label=label.strip(), user_id=current_user.id)
    db.session.add(new_routine)
    db.session.commit()
    return redirect(url_for('views.workouts'))

@views.route('/delete-routine/<int:id>', methods=['POST'])
@login_required
def delete_routine(id):
    routine = Routine.query.get_or_404(id)
    if routine.user_id != current_user.id:
        return "Unauthorized", 403
    db.session.delete(routine)
    db.session.commit()
    return redirect(url_for('views.workouts'))

@views.route('/add-day', methods=["POST"])
@login_required
def add_day():
    label = request.form['label']
    if not label.strip():
        return "Routine label required", 400
    
    new_day = Routine(label=label.strip(), user_id=current_user.id)
    db.session.add(new_day)
    db.session.commit()
    return redirect(url_for('views.meal'))

@views.route('/meal', methods=['GET', 'POST'])
@login_required
def meal():
    if request.method == "POST":
        category =  request.form['category']
        name = request.form['name']
        serving_size = request.form['serving_size']
        day_id = int(request.form['day_id'])

        new_meal = Meal(
            category = category,
            name = name,
            serving_size = serving_size,
            day_id = day_id
        )

        db.session.add(new_meal)
        db.session.commit

    elif request.method == "GET":
        return render_template('meal.html', user=current_user)

@views.route('/weight')
@login_required
def weight():
    return render_template('weight.html', user=current_user)

