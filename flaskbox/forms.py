from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class DnsLookupForm(FlaskForm):
    hostname = StringField('hostname', validators=[DataRequired()])

