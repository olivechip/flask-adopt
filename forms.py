from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available?")
