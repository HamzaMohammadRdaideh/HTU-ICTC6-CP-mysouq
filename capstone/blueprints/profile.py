from flask import Blueprint, render_template, request, redirect, session, flash , url_for
from flask_wtf import FlaskForm
from capstone.models import User , BuyRequest
from bson.objectid import ObjectId
from .user import disable_user , login_required , maintenance


# define our blueprint
profile_bp = Blueprint('profile', __name__)

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

    
    user = User.objects(id = user_id).first()
    user.delete()

    flash(f"Account '{user.username}' has been deleted.!")

    return redirect(url_for('profile.display_users'))


@profile_bp.route('/disable_user/<user_id>', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user    
def disable_user_list(user_id) :
    
    user = User.objects(id = user_id).first()
    
    user.disable = True

    user.save()

    flash(f"Account '{user.username}' has been disabled.!")


    return redirect(url_for('profile.display_users'))


@profile_bp.route('/unlock_disable_user/<user_id>', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user    
def unlock_disable_user_user_list(user_id) :
    
    user = User.objects(id = user_id).first()
    
    user.disable = False

    user.save()

    flash(f"Account '{user.username}' has been unlocked.!")


    return redirect(url_for('profile.display_users'))


@profile_bp.route('/profile/maintenance', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user    
def maintenance_mode() :

    User.objects(role = 0 and 1).update(maintenance = True) 
    flash('The Website now in Maintenance!')

    return redirect(url_for('profile.profile'))


@profile_bp.route('/profile/remove_maintenance_mode', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user    
def remove_maintenance_mode() :
    
    User.objects(role = 0 and 1).update(maintenance = False) 

    flash('The Website now on!')
    
    return redirect(url_for('profile.profile'))


@profile_bp.route('/disable_users_list', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user   
def disabled_list():

    users = User.objects(disable = True)

    return render_template('profile/blocked_list.html' , users = users, title = "Blocked-List" , icon = 'fas fa-users')
    

@profile_bp.route('/buy_request_list/<user_id>', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user  
def buy_request_list(user_id):

    user = User.objects()
    list_request = BuyRequest.objects(id == user_id)

    return render_template('profile/buy_request_list.html' , user = user , list_request = list_request ,title = 'Buy-Request' , icon = 'fas fa-shopping-cart')
