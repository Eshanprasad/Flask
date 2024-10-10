from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

""" we'll be actually writing python classes, that will be representative of our forms and will be converted
into html forms within our template

"""

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])  # Username is a label

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])  # can also put min and max password length restriction, but we are not using that as of now 

    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')]) #we want to make sure that the password and confirm_password are same, so we need to use Equalto validator 

    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])  # can also put min and max password length restriction, but we are not using that as of now 

    remember = BooleanField('Remember Me')  #this will allow users to stay logged in for some time after their browser closes using a secure cookie. # 'Remember Me' is just a label name

    submit = SubmitField('Login')


    """ when we use these forms, we need to set a secret key for our application
        A secret key will protect against modifying cookies and cross site requests, forgery attacks and manymore.
        

    """