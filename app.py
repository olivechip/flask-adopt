from flask import Flask, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask-wtf import FlaskForm
from models import db, connect_db

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'chocobo_stable'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_ECHO'] = True

toolbar = DebugToolbarExtension(app)
connect_db(app)
app.app_context().push()
