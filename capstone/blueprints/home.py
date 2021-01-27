from flask import Blueprint, render_template, request, redirect, session, flash , url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField
from capstone.forms import LoginForm
from capstone.models import User , Item

# define our blueprint
home_bp = Blueprint('home', __name__)


@home_bp.route('/home', methods=['POST', 'GET'])
def home():

    items = Item.objects()

    return render_template('item/home.html', items = items)