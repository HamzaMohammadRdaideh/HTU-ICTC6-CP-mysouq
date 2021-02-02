from flask import Blueprint, render_template, request, redirect, session, flash , url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField
from capstone.forms import LoginForm
from capstone.models import User , Item , BuyRequest
from .user import disable_user , login_required , maintenance

# define our blueprint
notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/notification/view_buy_request', methods=['POST', 'GET'])
# @maintenance
# @login_required
# @disable_user
def view_buy_request():

    current_user = User.objects(id = session['user']['id']).first()
    my_items = Item.objects(user = current_user)
    
    my_buy_requests = []
    for item in my_items:
            
        my_buy_requests.append(BuyRequest.objects(item = item))
 
    return render_template("notifications/view_my_buy_request.html" , my_buy_requests = my_buy_requests , title = 'Notifications-View')


# @notification_bp.route('/notification/<item_id>/approve_buy_request/<request_id>', methods=['POST', 'GET'])
# @maintenance
# @login_required
# @disable_user
# def approve_buy_request(item_id,request_id ):

    # current_user = User.objects(id = session['user']['id']).first()
    # my_items = Item.objects(user = current_user)
    
    # print(my_items)
    # my_buy_requests = []
    # for item in my_items:
            
    #     my_buy_requests.append(BuyRequest.objects(item = item))

    # print(request_id)
    # # item = Item.objects(id = item_id).first()
    # # item.sold = True
    # # item.save()
    # Item.objects(id = item_id).update_one(pull__buy_request_list = request_id)
    

    # return render_template("notifications/review-my-buy-request.html" , my_buy_requests = my_buy_requests)