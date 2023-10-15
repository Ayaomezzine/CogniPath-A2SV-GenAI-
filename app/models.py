# -*- encoding: utf-8 -*-
"""
Copyright : COGNIPATH 2023
"""

from app         import db
from flask_login import UserMixin
from enum import Enum

import sqlite3
from datetime import datetime

DATABASE = './app/db.sqlite3'
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

def get_activities_count_by_day():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    activity_counts = [0] * 7  # Initialize the list with zeros for each day of the week

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # SQL query to count activities by day of the week
        query = """
        SELECT strftime('%w', date_time) as day, COUNT(*) as count
        FROM activities
        GROUP BY day
        """
        cursor.execute(query)

        for row in cursor.fetchall():
            day_index = int(row[0])
            activity_count = int(row[1])
            activity_counts[day_index] = activity_count

        return activity_counts
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

    finally:
        conn.close()

def get_activities_count_by_week():
    activity_counts = [0,0,0,0,0,0,0,0,0]

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # SQL query to count activities by week for the last 9 weeks
        query = """
        SELECT strftime('%W', date_time) as week, COUNT(*) as count
        FROM activities
        WHERE date_time >= date('now', '-9 weeks')
        GROUP BY week
        """
        cursor.execute(query)

        for row in cursor.fetchall():
            week_number = int(row[0])
            activity_count = int(row[1])
            activity_counts.append((week_number, activity_count))

        return activity_counts

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

    finally:
        conn.close()


def get_activities_count_by_month():
    activity_counts = [0] * 9  # Initialize the list with zeros for each month
    month_labels = []

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # SQL query to count activities by month for the last 9 months
        query = """
        SELECT strftime('%Y-%m', date_time) as month, COUNT(*) as count
        FROM activities
        WHERE date_time >= date('now', '-9 months')
        GROUP BY month
        """
        cursor.execute(query)

        for row in cursor.fetchall():
            month = row[0]
            activity_count = int(row[1])

            # Determine the index of the month in the last 9 months
            # For example, if you're in October, the index would be 0 for October, 1 for September, and so on.
            current_month = cursor.execute("SELECT strftime('%Y-%m', 'now')").fetchone()[0]
            month_index = (int(current_month[:4]) - int(month[:4])) * 12 + int(current_month[5:]) - int(month[5:])

            # Update the count for the respective month
            activity_counts[month_index] = activity_count

            # Get the month label (e.g., "Feb") and add it to the labels list
            month_label = datetime.strptime(month, "%Y-%m").strftime("%b")
            month_labels.append(month_label)

        return activity_counts, month_labels

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

    finally:
        conn.close()

def get_recent_activities():
    try:
        conn = sqlite3.connect(DATABASE)  # Replace with your database path
        cursor = conn.cursor()

        # SQL query to select the 6 most recent activities
        query = """
        SELECT *
        FROM activities
        ORDER BY date_time DESC
        LIMIT 6
        """
        cursor.execute(query)
        recent_activities = cursor.fetchall()

        return recent_activities

    except Exception as e:
        print("An error occurred: ",str(e))
        return None

    finally:
        conn.close()