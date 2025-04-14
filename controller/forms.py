from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, EmailField,validators, SelectField
from wtforms.validators import InputRequired



class addTaskForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    office_number = StringField('office_name', validators=[InputRequired()])
    department = StringField('deparrtment', validators=[InputRequired()])
    challange = TextAreaField('challenge', validators=[InputRequired()])
    submit = SubmitField(label='Send your Query')
    
    
class loginForm(FlaskForm):
    username = EmailField('username', validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    submit = SubmitField(label='Login')
    
    
class addTeamMember(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
    username =  StringField('username', validators=[InputRequired()])
    system_role = SelectField('Choose role', choices=['Administrator','General User'], validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()] )
    password = PasswordField(validators=[InputRequired()])
    submit = SubmitField(label='Add team Member')

    
    
