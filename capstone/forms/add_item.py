from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField, FloatField, SelectField, FileField


class AddItemForm(FlaskForm):

    title = StringField("Title: ", [validators.InputRequired()])

    description = TextAreaField("Description: ", [validators.InputRequired()])

    price = FloatField("Price: ", [validators.InputRequired()])

    category = SelectField("Category: ", choices=[('1', 'Clothes'), ('2', 'Vehicles'), ('3', 'Digital Devices')])

    image = FileField()

    submit = SubmitField("Add Item")