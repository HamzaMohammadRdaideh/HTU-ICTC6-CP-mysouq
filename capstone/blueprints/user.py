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
    @wraps(function)
    def check_required(*args, **kwargs):

        if  session['user']['id'] :
            return function(*args, **kwargs)

        else:
            return redirect(url_for('login.login'))

    return check_required


def disable_user(function):
    @wraps(function)
    def check(*args, **kwargs):

        if session['user']['disable'] == False:
            return function(*args, **kwargs)

        else:
            return render_template('user/disable.html')
    return check


def maintenance(function):
    @wraps(function)
    def check(*args, **kwargs):

        if session['user']['maintenance'] == False:
            return function(*args, **kwargs)

        else:
            return render_template('user/maintenance.html')
    return check

    
@user_bp.route('/user/edit_profile', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user
def edit_profile_user():

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
@maintenance
@login_required
@disable_user
def change_password():

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




