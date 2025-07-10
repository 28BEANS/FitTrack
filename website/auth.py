from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth =  Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>This is the logout page</p>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('first_name')
        lastName = request.form.get('last_name')
        bday = request.form.get('bday')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email is already registered.", category='error')
        elif len(email) < 4:
            flash("Email must be more than 3 characters.", category='error')
        elif len(firstName) < 2 or len(lastName) < 2:
            flash("First and last name must be greater than 1 character", category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
        else:
            new_user = User(email=email, first_name=firstName, last_name=lastName, birth_day=bday, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash("Account succesfully created!", category='success')
            return redirect(url_for('views.home'))

        
    return render_template('signup.html')


