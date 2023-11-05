from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    artist = StringField(validators=[DataRequired()])
    submit = SubmitField(name="Ruin Eloquently")
