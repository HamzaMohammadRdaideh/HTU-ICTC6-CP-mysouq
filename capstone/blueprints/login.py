from flask import Blueprint, render_template, request, redirect, session, flash , url_for
from flask_wtf import FlaskForm
from capstone.forms import LoginForm
from capstone.models import User


# define our blueprint
login_bp = Blueprint('login', __name__)

@login_bp.route("/" , methods = ['POST' , 'GET'])
@login_bp.route('/login', methods=['POST', 'GET'])
def login():
    """This function validates the user's login credentials then takes them to the Home page."""
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

        return redirect(url_for('profile.profile'))

    # render the login template
    return render_template('login/login.html', form = login_form , icon = 'fas fa-sign-in-alt' , title = 'Log-In')


@login_bp.route('/session')
def show_session():
    """This function prints out the Session dictionary.
    This is only accessable through the URL and is used by the site developers for testing."""
    return dict(session)


@login_bp.route('/logout')
def logout():
    """This function removes the logged in user's information from the Session dictionary."""
    # clear all data from session
    session.clear()

    # redirect to index
    return redirect(url_for('login.login'))
