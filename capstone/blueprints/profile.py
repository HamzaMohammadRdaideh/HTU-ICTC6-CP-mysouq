from flask import Blueprint, render_template, request, redirect, session, flash , url_for
from flask_wtf import FlaskForm
from capstone.models import User , BuyRequest ,Item , UpgradeRequest ,Category
from bson.objectid import ObjectId
from .user import disable_user , login_required , maintenance
from capstone.forms.items import AddCategoryForm

# define our blueprint
profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['POST', 'GET'])
@login_required
@disable_user
@maintenance
def profile():

    user = User.objects(id = session["user"]['id']).first()

    return render_template('profile/profile.html' , user = user)


@profile_bp.route('/display_users', methods=['POST', 'GET'])
@login_required
@disable_user
@maintenance
def display_users():

    users = User.objects()

    return render_template('profile/display_users.html' , users = users , title = 'All-Users' , icon = 'fas fa-users')


@profile_bp.route('/remove_user/<user_id>', methods=['POST', 'GET'])
@login_required
@disable_user
@maintenance
def remove_user(user_id):

    
    user = User.objects(id = user_id).first()
    user.delete()

    flash(f"Account '{user.username}' has been deleted.!")

    return redirect(url_for('profile.display_users'))


@profile_bp.route('/disable_user/<user_id>', methods=['POST', 'GET'])
@login_required
@disable_user
@maintenance    
def disable_user_list(user_id) :
    
    user = User.objects(id = user_id).first()
    
    user.disable = True

    user.save()

    flash(f"Account '{user.username}' has been disabled.!")


    return redirect(url_for('profile.display_users'))


@profile_bp.route('/unlock_disable_user/<user_id>', methods=['POST', 'GET'])
@login_required
@disable_user
@maintenance    
def unlock_disable_user_user_list(user_id) :
    
    user = User.objects(id = user_id).first()
    
    user.disable = False

    user.save()

    flash(f"Account '{user.username}' has been unlocked.!")


    return redirect(url_for('profile.display_users'))


@profile_bp.route('/profile/maintenance', methods=['POST', 'GET'])
@login_required
@disable_user
@maintenance    
def maintenance_mode() :

    User.objects(role = 0 and 1).update(maintenance = True) 
    flash('The Website now in Maintenance!')

    return redirect(url_for('profile.profile'))


@profile_bp.route('/profile/remove_maintenance_mode', methods=['POST', 'GET'])
@login_required
@disable_user
@maintenance    
def remove_maintenance_mode() :
    
    User.objects(role = 0 and 1).update(maintenance = False) 

    flash('The Website now on!')
    
    return redirect(url_for('profile.profile'))


@profile_bp.route('/disable_users_list', methods=['POST', 'GET'])
@login_required
@disable_user
@maintenance  
def disabled_list():

    users = User.objects(disable = True)

    return render_template('profile/blocked_list.html' , users = users, title = "Blocked-List" , icon = 'fas fa-users')
    

@profile_bp.route('/buy_request_list/<user_id>', methods=['POST', 'GET'])
@login_required
@disable_user
@maintenance 
def buy_request_list(user_id):


    list_request = BuyRequest.objects(user = session['user']['id'])

    return render_template('profile/buy_request_list.html'  , list_request = list_request ,title = 'Buy-Request' , icon = 'fas fa-shopping-cart')



@profile_bp.route('/user/favorite_list', methods=['GET', 'POST'])
# @login_required
# @disable_user
# @maintenance 
def view_favorite():

    favorite_items = User.objects(id = session['user']['id']).get().favorite

    items = []
   
    for item in range(0 ,len(favorite_items)):

        item = Item.objects(id = favorite_items[item]).first()

        items.append(item)
        
    
    return render_template("profile/user_favorite_items.html" , items = items , title = 'Favorites-Items' , icon = 'fas fa-star')


# @profile_bp.route('/request_upgrade', methods=['GET', 'POST'])
# @login_required
# @disable_user
# @maintenance 
# def request_upgrade():

#     request = UpgradeRequest.objects(user = session['user']['id']).first()

#     if not request:

#         upgrade_request = UpgradeRequest(user = session['user']['id'], status = "Pending")

#         upgrade_request.save()

#     else:

#         flash("You have already requested an upgrade.")

#     return redirect(url_for('profile.profile'))


@profile_bp.route('/add_category', methods=['GET', 'POST'])
@login_required
@disable_user
@maintenance
def add_category():

    add_category_form = AddCategoryForm()

    if add_category_form.validate_on_submit():


        category_value = add_category_form.value.data
        category_label = add_category_form.label.data

        new_category = Category( value = category_value, label = category_label)

        new_category.save()
        
        flash('New Category has been added.!')

        return redirect(url_for("profile.profile"))

    return render_template("profile/add_category.html", form = add_category_form)



