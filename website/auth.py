from flask import Blueprint, render_template, request, flash

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

        if len(email) < 4:
            flash("Email must be more than 3 characters.", category='error')
        elif len(firstName) < 2 or len(lastName) < 2:
            flash("First and last name must be greater than 1 character", category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
        else:
            flash("Account succesfully created!", category='success')
        
    return render_template('signup.html')


