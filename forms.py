from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import ValidationError, InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld=True, message='Please enter a valid url.')])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available?")

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld=True, message='Please enter a valid url.')])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available?")