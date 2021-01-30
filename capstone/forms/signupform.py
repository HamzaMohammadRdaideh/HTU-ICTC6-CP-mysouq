from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators ,PasswordField ,TextAreaField 
from wtforms.fields.html5 import EmailField , DateField 

# Sign Up Account Settings Forms
class SignUpForm(FlaskForm):

    username = StringField("Username : ", [validators.InputRequired()] , render_kw={"placeholder": "User Name"})
    first_name = StringField("First name : " , render_kw={"placeholder": "First Name"})
    last_name = StringField("Last name : " , render_kw={"placeholder": "Last Name"})
    password = PasswordField("Password : ", [validators.InputRequired()] , render_kw={"placeholder": "**********"})
    email = EmailField("Email : " , [validators.InputRequired()] , render_kw={"placeholder": "Email"})
    birthday = DateField("Birthday : " , [validators.InputRequired()] , format='%Y-%m-%d')
    submit = SubmitField("Sign-Up")    