from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import FlaskForm
from models import db, connect_db, Pet

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'chocobo_stable'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
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
    return render_template('list_pets.html')