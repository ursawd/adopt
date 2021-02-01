from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "SECRET!"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pets"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True


connect_db(app)
# db.create_all()

from flask_debugtoolbar import DebugToolbarExtension

debug = DebugToolbarExtension(app)


@app.route("/")
def list_pets():
    """List pets"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def show_process_pet_form():
    """Display / process add a pet form"""

    form = AddPetForm()  # create instance of add a pet form

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data
        pet1 = Pet(
            name=name,
            species=species,
            photo_url=photo,
            age=age,
            notes=notes,
            available=True,
        )
        db.session.add(pet1)
        db.session.commit()
        flash(f"Added {name} to Pets List")
        return redirect("/")
    else:
        # GET route processing
        return render_template("add-pet.html", form=form)
