from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class HostLookupForm(FlaskForm):
    host = StringField('host', validators=[DataRequired()])
