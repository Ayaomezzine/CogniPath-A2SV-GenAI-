# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app         import db
from flask_login import UserMixin
from enum import Enum

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id       = db.Column(db.Integer,     primary_key=True)
    user     = db.Column(db.String(64),  unique = True)
    email    = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(500))

    #Added fields
    progression = db.Column(db.Integer)
    Language = db.Column(db.Integer)
    Intellect = db.Column(db.Integer)
    Social_Skills = db.Column(db.Integer)
    pathology = db.Column(db.String(100))
    isPremium = db.Column(db.Boolean)

    def __init__(self, user, email, password, progression, Language, Intellect, Social_Skills, pathology, isPremium):
        self.user = user
        self.password = password
        self.email = email
        self.progression = progression
        self.Language = Language
        self.Intellect = Intellect
        self.Social_Skills = Social_Skills
        self.pathology = pathology
        self.isPremium = isPremium

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)

    def save(self):
        # Check if any of the attributes is None or an empty string
        if self.user is None or self.email is None or self.password is None:
            raise ValueError("User, email, and password must be provided.")
        # Save the user object
        db.session.add(self)
        db.session.commit()

        return self
    
class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    title = db.Column(db.String(20))
    input = db.Column(db.String(200))
    output = db.Column(db.String(200))
    user_email = db.Column(db.String(50))
    activity = db.Column(db.String(20))
    social_score = db.Column(db.Integer)
    intellect_score = db.Column(db.Integer)
    language_score = db.Column(db.Integer)
    avg_score = db.Column(db.Integer)

    def __init__(self, title, input, output, user_email, activity, social_score, intellect_score, language_score, avg_score):
        self.title = title
        self.input = input
        self.output = output
        self.user_email = user_email
        self.activity = activity
        self.social_score = social_score
        self.intellect_score = intellect_score
        self.language_score = language_score
        self.avg_score = avg_score

    def __repr__(self):
        return f"Activity(id={self.id}, title='{self.title}', user_email='{self.user_email}', date_time='{self.date_time}')"
    
    def save(self):
        """
        Save the activity record to the database.
        """
        db.session.add(self)  # Add the activity object to the current session
        db.session.commit()   # Commit the transaction to save the record

def update_user_scores(user_email):
    """
    Update the intellect, social, language, and progress columns in the Users table
    based on the corresponding values from the activities table for a specific user's email.
    """
    # Calculate the updated scores based on activities for the given user's email
    user_activities = Activity.query.filter_by(user_email=user_email).all()

    # Initialize scores
    intellect_score = 0
    social_score = 0
    language_score = 0
    avg_progress = 0
    count = 0

    for activity in user_activities:
        intellect_score += activity.intellect_score
        social_score += activity.social_score
        language_score += activity.language_score
        avg_progress += activity.avg_score
        count +=1
        # You can calculate progression based on your business logic here

    # Update the user's scores in the Users table
    user = Users.query.filter_by(email=user_email).first()

    if user:
        user.Intellect = intellect_score
        user.Social_Skills = social_score
        user.Language = language_score
        user.progression = avg_progress  # Update based on your logic

        # Save the changes to the database
        db.session.commit()
    else:
        # Handle the case where the user with the specified email does not exist
        pass

    return count