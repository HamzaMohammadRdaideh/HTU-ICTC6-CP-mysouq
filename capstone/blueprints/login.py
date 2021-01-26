from flask import Blueprint, render_template, request, redirect, session, flash , url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField
from capstone.forms import LoginForm
from capstone.models import User

# define our blueprint
login_bp = Blueprint('login', __name__)

@login_bp.route("/" , methods = ['POST' , 'GET'])
@login_bp.route('/login', methods=['POST', 'GET'])
def login():

    # created an instance of our form
    login_form = LoginForm()

    # check if it is a form submission
    if login_form.validate_on_submit():

        # read values from the login wtform
        username = login_form.username.data
        password = login_form.password.data

        user = User.objects(username=username).first()

        # check if credentials are valid
        if (user) and (user.authenticate(username, password)):
            session['user'] = user.serialize()

            # redirect the user after login
            return redirect(url_for('home.home'))
        else:
            # invalid credentials, redirect to login with error message
            flash("Login invalid. Please check your username and password.")
            return redirect(url_for('login.login'))


        return redirect("/profile")

    # render the login template
    return render_template('login/login.html', form=login_form)


@login_bp.route('/session')
def show_session():
    return dict(session)


@login_bp.route('/logout')
def logout():

    # pop 'uid' from session
    session.clear()

    # redirect to index
    return redirect("/")
