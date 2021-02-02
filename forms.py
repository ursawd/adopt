from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional
from flask_wtf.file import FileField


class PetForm(FlaskForm):
    """Form for adding a pet to db"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField(
        "Species", choices=[("Dog", "dog"), ("Otter", "otter"), ("Rabbit", "rabbit")], validators=[InputRequired()]
    )
    # ? Too much trouble during during dev to enforce URL restriction for images
    # ? Not enforcing URL allow use of images in /static/imgs
    # photo = StringField("Photo URL", validators=[URL(require_tld=False), Optional()])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])


class EditPet(FlaskForm):
    """Form to edit some pet information"""

    photo_url = StringField("Photo URL", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    # ?    with following line, available was required to checked
    #    available = BooleanField("Available", validators=[InputRequired()])
    available = BooleanField("Available")
    filename = FileField("File Upload")
