from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms import validators
from wtforms.fields.core import RadioField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us a little about yourself', validators = [Required()])
    submit = SubmitField('Submit')