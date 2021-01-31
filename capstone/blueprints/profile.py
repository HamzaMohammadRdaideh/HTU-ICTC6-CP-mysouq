from flask import Blueprint, render_template, request, redirect, session, flash , url_for
from flask_wtf import FlaskForm
from capstone.models import User
from bson.objectid import ObjectId
from .user import disable_user , login_required , maintenance


# define our blueprint
profile_bp = Blueprint('profile', __name__)

@profile_bp.route("/" , methods = ['POST' , 'GET'])
@profile_bp.route('/profile', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user
def profile():

    user = User.objects(id = session["user"]['id']).first()

    return render_template('profile/profile.html' , user = user)


@profile_bp.route('/display_users', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user
def display_users():

    users = User.objects()

    return render_template('profile/display_users.html' , users = users , title = 'All-Users' , icon = 'fas fa-users')


@profile_bp.route('/remove_user/<user_id>', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user
def remove_user(user_id):

    User.objects(id = user_id).first().delete()

    return redirect(url_for('profile.display_users'))


@profile_bp.route('/disable_user/<user_id>', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user    
def disable_user_list(user_id) :
    
    user = User.objects(id = user_id).first()
    
    user.disable = True

    user.save()

    return redirect(url_for('profile.display_users'))


@profile_bp.route('/profile/maintenance', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user    
def maintenance_mode() :

    User.objects(role = 0 and 1).update(maintenance = True) 
    
    return redirect(url_for('profile.profile'))


@profile_bp.route('/profile/remove_maintenance_mode', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user    
def remove_maintenance_mode() :
    
    User.objects(role = 0 and 1).update(maintenance = False) 
    
    return redirect(url_for('profile.profile'))