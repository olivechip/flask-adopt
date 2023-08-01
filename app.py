from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'chocobo_stable'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SQLALCHEMY_ECHO'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()    
db.create_all()

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/pets')
def list_pets():
    pets = Pet.query.all()
    return render_template('list_pets.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name}, the {species}!")
        return redirect('/pets')
    else:
        return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f"Edited {pet.name}, the {pet.species}!")
        return redirect('/pets')
    else:
        pet = Pet.query.get_or_404(pet_id)
        return render_template('pet_details.html', pet=pet, form=form)