# Import necessary modules
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Define the Note model
class Note(db.Model):
    # Define columns for the Note model
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000000000)) # Text content of the note, with large capacity
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # Date and time the note was created
    user_id = db.Column(db.Integer, db.ForeignKey("user.id")) # Foreign key to associate note with a user

# Define the User model
class User(db.Model, UserMixin):
    # Define columns for the User model
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # Email of the user, unique
    password = db.Column(db.String(150)) # Password of the user
    first_name = db.Column(db.String(150)) # First name of the user
    notes = db.relationship("Note") # Relationship to associate users with their notes