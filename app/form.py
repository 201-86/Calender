from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Optional, ValidationError
import app.models
from wtforms.fields import DateField, DateTimeField


class Add_User(FlaskForm):
    username = StringField('title', validators=[DataRequired()])
    password = StringField('description', validators=[DataRequired()])


class Add_date(FlaskForm):
#    year = IntegerField('year', validators=[DataRequired()])
#    month = IntegerField('month', validators=[DataRequired()])
#    day = IntegerField('day', validators=[DataRequired()])
    date = DateField('date', format = '%Y-%m-%d')
    message = StringField('message')

class changedate(FlaskForm):
    month = SelectField(choices=[(0, "January"), (1, "February"), (2, "March"), (3, "April"), (4, "May"), (5, "June"), (6, "July"), (7, "August"), (8, "September"), (9, "October"), (10, "November"), (11, "December")])
