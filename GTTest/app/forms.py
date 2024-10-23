from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField, TextAreaField, validators, FloatField
from wtforms.validators import ValidationError, DataRequired, ValidationError, Length, Email, EqualTo, Regexp
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('User Details', validators=[DataRequired(message='Incorect Username')])
    password = PasswordField('Password', validators=[DataRequired(message='Incorrect Password')])
    submit = SubmitField('Login')


class Signup(FlaskForm):
    username = StringField('Username', [validators.DataRequired(message="Username must be at least 5 characters long"), Regexp("^[A-Za-z][A-Za-z0-9_.]*$",
                0, "Usernames must be a combination of letters, numbers, dots or underscores!!!")])
    email =  EmailField('Email', [validators.Email(message='Enter a valid Email addrress!!!')])
    password = PasswordField('Password', [validators.DataRequired(message="use a strong combination!!!"), validators.Length(min=8, max=15)])
    password2 = PasswordField('Confirm Password',[validators.DataRequired(message="Re-enter password!!!"),validators.EqualTo('password', message='Mismatched Passwords!!!')])
    #profile_pic = FileField('Profile Picture', validators=[FileRequired(message="Upload a photo!!!"), FileAllowed(['jpg','png'],'Images Only!!!')])
    submit = SubmitField('Sign Up')
    
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Sorry, username already exists!!!')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Sorry, email address already in use!!!')

class NewBags(FlaskForm):
    name = StringField('Name of Bag', validators=[DataRequired(message="You can't create an inventory without a name!")])
    Description = TextAreaField('About Bag', validators=[DataRequired(message="inventory must have a description!")])
    Price = FloatField('Price', validators=[DataRequired(message="inventory must have a price!")] )
    submit = SubmitField('Create Inventory')