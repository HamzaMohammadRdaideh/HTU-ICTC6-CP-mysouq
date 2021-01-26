from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators ,PasswordField ,TextAreaField ,EmailField ,DateTimeField

# Sign Up Account Settings Forms
class SignUpForm(FlaskForm):

    username = StringField("Username : ", [validators.InputRequired()])
    password = PasswordField("Password : ", [validators.InputRequired()])
    email = EmailField("Email : " , [validators.InputRequired()])
    brithday = DateTimeField("Brithday : " , [validators.InputRequired()])
    submit = SubmitField("Sign-Up")    