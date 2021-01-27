from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators,PasswordField, TextAreaField 
from wtforms.validators import InputRequired, EqualTo, Length

# Edit profile Forms
class EditProfileForm(FlaskForm):

    new_first_name = StringField("New first name : ")
    new_last_name = StringField("New last name : ")
    submit = SubmitField("Save Changes")


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Enter your current password', [InputRequired()])
    new_password = PasswordField('Enter your new password', [InputRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField("Confirm your new password", [InputRequired()])
    change_password = SubmitField("Change password")
