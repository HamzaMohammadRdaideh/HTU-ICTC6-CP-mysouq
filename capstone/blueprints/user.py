from flask import Blueprint, render_template, request, redirect, session, flash , url_for 
from flask_wtf import FlaskForm
from capstone.models import User
from capstone.forms.edit_profile import EditProfileForm  , ChangePasswordForm
from bson import ObjectId

# define our blueprint
user_bp = Blueprint('user', __name__)


@user_bp.route('/user/edit_profile', methods=['POST', 'GET'])
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

        return redirect(url_for('home.home')) 

    return render_template("user/edit_profile_user.html", form = edit_profile_form)


@user_bp.route('/user/change_password', methods=['GET', 'POST'])
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
            return redirect(url_for('user.change_password'))

    return render_template("user/change_password.html", form=change_password_form)



