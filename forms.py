from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField


class AddPetForm(FlaskForm):
    """Form for adding a pet to db"""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo = StringField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes")