from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


def character_check(form, field):
    excluded_chars = './\\^'
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed.")

class PostForm(FlaskForm):
    title = StringField(validators=[DataRequired(), character_check])
    artist = StringField(validators=[DataRequired(), character_check])
    submit = SubmitField()