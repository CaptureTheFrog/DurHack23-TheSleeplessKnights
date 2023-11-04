from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LyricForm(FlaskForm):
    song_name = StringField("name", validators=[DataRequired()])
    artist_name = StringField("name", validators=[DataRequired()])
    submit = SubmitField()
