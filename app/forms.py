from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactF(FlaskForm):
     name=StringField('Name', validators=[DataRequired()])
     email=StringField('Email', validators=[DataRequired(), Email()])
     subject=StringField('Subject', validators=[DataRequired()])
     msg=TextAreaField('Message', validators=[DataRequired()])