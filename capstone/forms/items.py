from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField, FloatField, SelectField, FileField


class AddItemForm(FlaskForm):

    title = StringField("Title: ", [validators.InputRequired()] , render_kw={"placeholder": "Like Car For Sale"})

    description = TextAreaField("Description: ", [validators.InputRequired()] , render_kw={"placeholder": "Like Toyota Camry model 2020 , Color-Black "})

    price = FloatField("Price: ", [validators.InputRequired()] , render_kw={"placeholder": "00.00 JDS"})

    category = SelectField("Category: ", choices=[('1', 'Clothes'), ('2', 'Vehicles'), ('3', 'Digital Devices')])

    image = FileField()

    submit = SubmitField("Add Item")


class EditItemForm(FlaskForm):

    new_title = StringField("Title: ", [validators.InputRequired()])

    new_description = TextAreaField("Description: ", [validators.InputRequired()])

    new_price = FloatField("Price: ", [validators.InputRequired()])

    new_category = SelectField("Category: ", choices=[('1', 'Clothes'), ('2', 'Vehicles'), ('3', 'Digital Devices')])

    new_image = FileField()

    submit = SubmitField("Edit Item")    