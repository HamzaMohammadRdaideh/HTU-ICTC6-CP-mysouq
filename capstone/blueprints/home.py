from flask import Blueprint, render_template, request, redirect, session, flash , url_for
from flask_wtf import FlaskForm
from capstone.models import User , Item 
from capstone.forms.items import AddItemForm , EditItemForm
from bson import ObjectId


# define our blueprint
home_bp = Blueprint('home', __name__)






@home_bp.route('/home', methods=['POST', 'GET'])
def home():

    items = Item.objects()

    return render_template('item/home.html', items = items)



@home_bp.route('/user/add_item', methods=['GET', 'POST'])
def add_item():

    add_item_form = AddItemForm()

    if add_item_form.validate_on_submit():

        title = add_item_form.title.data
        description = add_item_form.description.data
        price = add_item_form.price.data
        category = add_item_form.category.data

        new_item = Item(title = title, description = description, price = price, category = category)
        
        new_item.save()

        flash("Your item has been successfully added.")

        return redirect(url_for('home.home'))

    return render_template("item/add_item.html", form = add_item_form , title = 'Add-Item' , icon="fa fa-upload")


@home_bp.route('/user/edit_item/<item_id>', methods=['GET', 'POST'])
def edit_item(item_id):

    edit_item_form = EditItemForm()

    item = Item.objects(id = item_id).first()

    if request.method == "GET":

        edit_item_form.new_title.data = item.title
        edit_item_form.new_description.data = item.description
        edit_item_form.new_price.data = item.price
        edit_item_form.new_category.data = item.category


    if edit_item_form.validate_on_submit():

        item.title = edit_item_form.new_title.data
        item.description = edit_item_form.new_description.data
        item.price = edit_item_form.new_price.data
        item.category = edit_item_form.new_category.data
        
        item.save()

        flash("Your item has been successfully edit.")

        return redirect(url_for('home.home'))

    return render_template("item/edit_item.html", form = edit_item_form)    

    
@home_bp.route('/user/delete_item/<item_id>', methods=['GET', 'POST'])
def delete_item(item_id):

    Item.objects(id = item_id).first().delete()

    return redirect(url_for("home.home"))  


@home_bp.route('/sort-item/date', methods=['GET', 'POST'])
def sort_date_items():

    items = Item.objects.order_by('-date')

    return render_template("item/home.html" , items = items)        


@home_bp.route('/sort-item/price', methods=['GET', 'POST'])
def sort_price_items():

    items = Item.objects.order_by('-price')

    return render_template("item/home.html" , items = items)    