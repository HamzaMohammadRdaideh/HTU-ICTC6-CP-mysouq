from flask import Blueprint, render_template, request, redirect, session, flash , url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField
from capstone.forms import SignUpForm
from capstone.models import User

# define our blueprint
signup_bp = Blueprint('signup', __name__)

@signup_bp.route("/signup" , methods = ['POST' , 'GET'])
def signup():
    """This function creates an account for a new user."""
    # created an instance of our form
    signup_form = SignUpForm()

    # check if it is a form submission
    if signup_form.validate_on_submit():

        #create instance from user model
        user = User()
        
        # read values from the login wtform
        user.username = signup_form.username.data
        user.first_name = signup_form.first_name.data
        user.last_name = signup_form.last_name.data
        user.password = user.encrypt_password(signup_form.password.data)
        user.email = signup_form.email.data
        user.birthday = signup_form.birthday.data

        # save the user object
        user.save()

        return redirect(url_for("login.login"))

    return render_template("sign-up/sign-up.html" , form = signup_form , title = 'Sign-Up' , icon = 'fas fa-user-plus')    
