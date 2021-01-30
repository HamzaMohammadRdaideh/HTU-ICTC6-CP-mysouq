from flask import Blueprint, render_template, request, redirect, session, flash , url_for
from flask_wtf import FlaskForm
from capstone.models import User


# define our blueprint
profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['POST', 'GET'])
def profile():

    user = User.objects(id = session["user"]['id']).first()

    return render_template('profile/profile.html' , user = user)


@profile_bp.route('/display_users', methods=['POST', 'GET'])
def display_users():

    users = User.objects()

    return render_template('profile/display_users.html' , users = users , title = 'All-Users' , icon = 'fas fa-users')


@profile_bp.route('/remove_user/<user_id>', methods=['POST', 'GET'])
def remove_user(user_id):

    User.objects(id = user_id).first().delete()

    return redirect('profile.display_users')