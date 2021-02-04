from flask import Blueprint, render_template, request, redirect, session, flash , url_for 
from flask_wtf import FlaskForm
from capstone.models import User , Item
from capstone.forms.edit_profile import EditProfileForm  , ChangePasswordForm
from capstone.forms.items import AddItemForm , EditItemForm
from bson import ObjectId
from functools import wraps

# define our blueprint
user_bp = Blueprint('user', __name__)


def login_required(function):
    """Login Decorator: 
    This function checks whether the user is logged in before accessing a functionality.
    If not; the user is taken to the Login Page."""
    @wraps(function)
    def check_required(*args, **kwargs):

        try:  
            session['user']['id'] 
            return function(*args, **kwargs)

        except:
            
            return redirect(url_for('login.login'))

    return check_required


def disable_user(function):
    """Disable Decorator: 
    This function checks whether the user "disable" attribute is set to "False" before accessing a functionality.
    If not; then the admin account has set this user's "disable" to "True" and is taken to the Disable Page."""
    @wraps(function)
    def check(*args, **kwargs):

        try:
            if session['user']['disable'] == False :
                return function(*args, **kwargs)

            else :
                return render_template('user/disable.html')
        except:
            return render_template('user/disable.html')
    
    return check


def maintenance(function):
    """Maintenance Decorator: 
    This function checks whether the user "maintenance" attribute is set to "False" before accessing a functionality.
    If not; then the admin account has set all users' "maintenance" to "True" and are taken to the Maintenance Page."""
    @wraps(function)
    def check(*args, **kwargs):

        try:
            if session['user']['maintenance'] == False:
                return function(*args, **kwargs)

            else :
                return render_template('user/maintenance.html')

        except:
            return render_template('user/maintenance.html')
    
    return check

    
@user_bp.route('/user/edit_profile', methods=['POST', 'GET'])
@login_required
@disable_user
@maintenance
def edit_profile_user():
    """This function provides the user with a form to edit their information."""
    user = User.objects(id = session["user"]['id']).first()

    edit_profile_form = EditProfileForm()
    
    if request.method == "GET":

    #set values in the form
        
        edit_profile_form.new_first_name.data = session['user']['first_name']
        edit_profile_form.new_last_name.data = session['user']['last_name']

    if  edit_profile_form.validate_on_submit():

        new_first_name = edit_profile_form.new_first_name.data
        new_last_name = edit_profile_form.new_last_name.data
    
        user.first_name = new_first_name
        user.last_name = new_last_name
        

        user.save()

        session['user'] = user.serialize()

        return redirect(url_for('profile.profile')) 

    return render_template("user/edit_profile_user.html", form = edit_profile_form , title = 'Edit-Profile' , icon = 'fas fa-user-edit')


@user_bp.route('/user/change_password', methods=['GET', 'POST'])
@login_required
@disable_user
@maintenance
def change_password():
    """This function allows the user to change/update their password
    It is a seperate functionality from "Edit Profile" for extra validation and seperation of concerns."""


    user = User.objects(id=session['user']['id']).first()

    change_password_form = ChangePasswordForm()

    if change_password_form.validate_on_submit():

        # read post values from the form
        current_password = change_password_form.current_password.data
        new_password = change_password_form.new_password.data

        if (user):
            user.change_password(current_password, new_password)
            user.save()
            flash("Your password has been successfully changed.")
            return redirect(url_for('profile.profile'))

    return render_template("user/change_password.html", form=change_password_form , title = 'Change-Password' , icon = 'fas fa-key') 




