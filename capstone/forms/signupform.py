from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators ,PasswordField ,TextAreaField
from wtforms.fields.html5 import EmailField , DateField

# Sign Up Account Settings Forms
class SignUpForm(FlaskForm):

    username = StringField("Username : ", [validators.InputRequired()])
    password = PasswordField("Password : ", [validators.InputRequired()])
    email = EmailField("Email : " , [validators.InputRequired()])
    birthday = DateField("Brithday : " , [validators.InputRequired()] , format='%Y-%m-%d')
    submit = SubmitField("Sign-Up")    