from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPet
import os

UPLOAD_FOLDER = "C:/Users/Phil/Google Drive/projects/UNITS/UNIT24/Unit24-1/WTFormsExercise/adopt/static/imgs/"

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.config["SECRET_KEY"] = "SECRET!"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pets"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True


connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension

debug = DebugToolbarExtension(app)


@app.route("/")
def list_pets():
    """List pets home page"""
    # get list of all pets in db, pass to home.html to display them
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def show_process_pet_form():
    """Display / process add a pet form"""

    # create instance of add a pet form
    form = PetForm()

    # validate form for CSRF, if GET route then validate fails
    if form.validate_on_submit():
        # POST route processing
        # get responses from form
        # name = form.name.data
        # species = form.species.data
        # photo_url = form.photo_url.data
        # age = form.age.data
        # notes = form.notes.data
        # # create instance of Pet
        # pet1 = Pet(
        #     name=name,
        #     species=species,
        #     photo_url=photo_url,
        #     age=age,
        #     notes=notes,
        #     available=True,
        # )

        pet2 = Pet()
        form.populate_obj(pet2)
        # add pet1 instance to db
        db.session.add(pet2)
        db.session.commit()
        # notify user pet added
        flash(f"Added {pet2.name} to Pets List")
        # go back to display all pets
        return redirect("/")
    else:
        # GET route processing
        # pass wtform form for display add pet
        return render_template("add-pet.html", form=form)


@app.route("/<int:pet_id_number>", methods={"GET", "POST"})
def edit_pet(pet_id_number):
    """Display and process pet edit form"""

    # get pet by id from db
    pet = Pet.query.get_or_404(pet_id_number)
    # take info from pet instance and use to populate
    # corresponding field in form
    form = EditPet(obj=pet)

    if form.validate_on_submit():

        # take form data and update pet instance
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        #! file upload in progress
        uploaded_file = request.files["filename"]
        if uploaded_file.filename != "":
            #            uploaded_file.save("/static/imgs", uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename))
        #! -----------------------
        # update pet instance in db
        db.session.add(pet)
        db.session.commit()

        # notify user pet edited
        flash(f"Edited {pet.name} on Pets List")

        # go back to display all pets
        return redirect("/")
    else:
        # GET route processing
        # pass pet instance to edit-pet.html so pet info can
        # be display that is defferent from info being edited. pass
        # wtform form to edit-pat.html so that certain info can be edited
        return render_template("edit-pet.html", pet=pet, form=form)
