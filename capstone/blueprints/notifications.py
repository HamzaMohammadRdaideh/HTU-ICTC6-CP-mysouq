from flask import Blueprint, render_template, request, redirect, session, flash , url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField
from capstone.models import User , Item , BuyRequest , UpgradeRequest
from .user import disable_user , login_required , maintenance

# define our blueprint
notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/notification/view_buy_request', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user
def view_buy_request():

    current_user = User.objects(id = session['user']['id']).first()
    my_items = Item.objects(user = current_user)
    
    my_buy_requests = []
    for item in my_items:
            
        my_buy_requests.append(BuyRequest.objects(item = item))
 
    return render_template("notifications/view_my_buy_request.html" , my_buy_requests = my_buy_requests , icon = 'fas fa-bell', title = 'Notifications-View')


@notifications_bp.route('/notification/<item_id>/approve_buy_request/<request_id>', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user
def approve_buy_request(item_id,request_id):
    """This function sets the "status" of a Buy Request to 'Approved'.
    Also, sets the "sold" attribute of the item to 'True'."""

    item = Item.objects(id = item_id).first()
    item.sold = True
    Item.objects(id = item_id).update_one(unset__buy_request_list = request_id)
    item.save()

    request = BuyRequest.objects(id = request_id).first()
    request.status = "Approved"
    request.save()

    flash("Item has been sold!")
    
    return redirect(url_for('notifications.view_buy_request'))



@notifications_bp.route('/notification/<item_id>/decline_request/<request_id>', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user
def decline_request(item_id,request_id):
    """This function sets the "status" of a Buy Request to 'Declined'."""
   
    Item.objects(id = item_id).update_one(unset__buy_request_list = request_id)

    request = BuyRequest.objects(id = request_id).first()
    request.status = "Declined"
    request.save()

    flash("Buy Request has been Declined!")
    
    return redirect(url_for('notifications.view_buy_request'))




@notifications_bp.route('/upgrade_request', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user
def upgrade_request():
    """This function is accessed when a Buyer user wants to become a Seller user.
    The function creates a request of type upgrade with a "Pending" status for them."""

    upgrade_request = UpgradeRequest(user = session['user']['id'], status = "Pending")

    upgrade_request.save()

    flash("Upgrade Request has been sent.")

    return redirect(url_for("profile.profile"))



@notifications_bp.route('/review_upgrade_requests', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user
def review_upgrade_requests():
    """This function is available for the Admin user to preview Upgrade Requests to choose to Approve or Decline."""

    users = User.objects()

    upgrade_requests = []

    for user in users:
        upgrade_requests.append(UpgradeRequest.objects(user = user).all())

    return render_template("notifications/review_upgrade_requests.html", upgrade_requests = upgrade_requests , title = 'Upgrade-Requests' , icon ='fas fa-level-up-alt')


@notifications_bp.route('/approve_upgrade_request/<request_id>', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user
def approve_upgrade_request(request_id):
    """This function sets the "status" of an Upgrade Request to 'Approved'.
    Also, sets the "role" of the user to '1' (Seller)."""

    request = UpgradeRequest.objects(id = request_id).first()
    request.status = "Approved"
    request.save()

    request.user.role = 1
    request.user.save()
    
    flash("Upgrade Request has been approved.")

    return redirect(url_for("notifications.review_upgrade_requests"))


@notifications_bp.route('/decline_upgrade_request/<request_id>', methods=['POST', 'GET'])
@maintenance
@login_required
@disable_user
def decline_upgrade_request(request_id):
    """This function sets the "status" of an Upgrade Request to 'Declined'.
    Also, sets the "role" of the user to '0' (Buyer). Just in case the Admin changed their mind """

    request = UpgradeRequest.objects(id = request_id).first()
    request.status = "Declined"
    request.save()

    flash("Upgrade Request has been declined.")
    

    return redirect(url_for("notifications.review_upgrade_requests"))