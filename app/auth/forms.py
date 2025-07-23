from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import User  # Make sure to import your User model

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email is required'),
        Email(message='Invalid email address')
    ], render_kw={"placeholder": "your@email.com"})
    
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required')
    ], render_kw={"placeholder": "••••••••"})
    
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login', render_kw={"class": "btn btn-primary"})

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email is required'),
        Email(message='Invalid email address'),
        Length(max=120, message='Email too long')
    ], render_kw={"placeholder": "your@email.com"})
    
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required'),
        Length(min=8, max=64, message='Password must be 8-64 characters'),
    ], render_kw={"placeholder": "••••••••"})
    
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(message='Please confirm your password'),
        EqualTo('password', message='Passwords must match')
    ], render_kw={"placeholder": "••••••••"})
    
    submit = SubmitField('Register', render_kw={"class": "btn btn-primary"})

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered. Please use a different email.')

class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email is required'),
        Email(message='Invalid email address')
    ], render_kw={"placeholder": "your@email.com"})
    
    submit = SubmitField('Request Password Reset')

class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired(message='Password is required'),
        Length(min=8, max=64, message='Password must be 8-64 characters'),
    ], render_kw={"placeholder": "••••••••"})
    
    confirm_password = PasswordField('Confirm New Password', validators=[
        DataRequired(message='Please confirm your password'),
        EqualTo('password', message='Passwords must match')
    ], render_kw={"placeholder": "••••••••"})
    
    submit = SubmitField('Reset Password')