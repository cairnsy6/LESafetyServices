from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField, DateField
from wtforms.validators import Length, Email, DataRequired, url


class MyForm(FlaskForm):
    name = StringField(label="Name")
    email = StringField(label='Email', validators=[Email(message="Please provide a valid email")])
    phone = StringField(label="Phone", validators=[Length(min=10, message="Please put in a valid number")])
    description = StringField(label="Reason for Enquiry")
    submit = SubmitField(label="Submit")

