"""Seed file to make sample data for Pet db."""

from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# create 3 pets
pet1 = Pet(
    name="Spot",
    species="dog",
    photo_url="/static/imgs/beagle.jpg",
    age=5,
    notes="This is a good looking beagle",
    available=True,
)
pet2 = Pet(
    name="Tiger",
    species="dog",
    photo_url="/static/imgs/rottwieller.jpg",
    age=5,
    notes="This is a bad looking beagle",
    available=False,
)
pet3 = Pet(
    name="Slick",
    species="otter",
    photo_url="/static/imgs/otter.jpg",
    age=1,
    notes="Very good swimmer",
    available=True,
)
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.commit()
