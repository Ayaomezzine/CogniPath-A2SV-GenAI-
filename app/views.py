# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Python modules
import os, logging 

# Flask modules
from flask               import render_template, request, url_for, redirect, send_from_directory,jsonify
from flask_login         import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2              import TemplateNotFound

# App modules
from app        import app, lm, db, bc
from app.models import Users, Activity, update_user_scores

#from app.forms  import LoginForm, RegisterForm
import requests
import os
import openai
import cv2
import numpy as np
from dotenv import load_dotenv
import base64
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
API_URL_trocr="https://api-inference.huggingface.co/models/microsoft/trocr-large-handwritten"
headers = {"Authorization": "Bearer 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"}

# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@login_required
@app.route('/back_index')
def back_index():
    # Access user attributes from the current_user object
    count_activities = update_user_scores(current_user.email)
    user_id = current_user.id
    username = current_user.user
    email = current_user.email
    progression = current_user.progression
    Language = current_user.Language
    Intellect = current_user.Intellect
    Social_Skills = current_user.Social_Skills
    pathology = current_user.pathology
    isPremium = current_user.isPremium

    # Render the dashboard template and pass the user data
    return render_template('dashboard.html', user=current_user, count_activities=count_activities)
# Logout user
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# Register a new user
@app.route('/auth', methods=['GET', 'POST'])
def register():
    msg = None
    success = False

    if request.method == 'POST':
        if 'signup' in request.form:  # Check if the signup form is submitted
            username = request.form['FullName']
            email = request.form['Email']
            password = request.form['mdp']
            pathology = request.form['pathology']

            # Check if the required fields are not empty
            if username and email and password:
                # Check if a user with the same username or email already exists
                user = Users.query.filter_by(user=username).first()
                user_by_email = Users.query.filter_by(email=email).first()

                if user or user_by_email:
                    msg = 'Error: User exists!'
                else:
                    pw_hash = bc.generate_password_hash(password)
                    user = Users(username, email, pw_hash,progression=0,Language=0,Intellect=0, Social_Skills=0,pathology='ASD',isPremium=False)
                    user.save()
                    msg = 'User created, please <a href="' + url_for('login') + '">login</a>'
                    success = True
            else:
                msg = 'Input error'

        elif 'signin' in request.form:  # Check if the signin form is submitted
            email_login = request.form['Email_login']
            password_login = request.form['mdp_login']

            # Check if the required fields are not empty
            if email_login and password_login:
                user = Users.query.filter_by(email=email_login).first()

                if user:
                    if bc.check_password_hash(user.password, password_login):
                        login_user(user)
                        return redirect(url_for('index'))
                    else:
                        msg = "Wrong password. Please try again."
                else:
                    msg = "Unknown user"
            else:
                msg = 'Input error'

    return render_template('login2.html', msg=msg, success=success)


# Authenticate user
@app.route('/login', methods=['GET', 'POST'])
def login():

    # Flask message injected into the page, in case of any errors
    msg = None
    
    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 

        # filter User out of database through username
        user = Users.query.filter_by(user=username).first()

        if user:
            
            if bc.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unknown user"

    return render_template( 'login2.html', form=form, msg=msg )

# App main route + generic routing
@app.route('/', defaults={'path': 'index'})
@app.route('/<path>')
def index(path):

    #if not current_user.is_authenticated:
    #    return redirect(url_for('login'))

    try:

        return render_template( 'index3.html')
    
    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# Return sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')



@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template('index3.html')




@login_required
@app.route("/generate", methods=["POST"])
def generate():
    selected_choice = request.form.get("choice")
    print("selected item:",selected_choice)
    activity = "Emotional Recognition"
    print("selected item:",selected_choice)
    # Define the payload for the Hugging Face API
    payload = {
        "inputs": selected_choice  # Use the selected choice as input
    }

    # Send a request to the Hugging Face API
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Check for any errors in the API response
        image_bytes = response.content

        new_activity = Activity(
            title=selected_choice,
            input=selected_choice,
            output="An image",
            user_email=current_user.email,
            activity=activity,
            social_score=10,
            intellect_score=20,
            language_score=30,
            avg_score=20
        )
        new_activity.save()
        update_user_scores(current_user.email)

        # Generate a unique filename for the image with a .jfif extension
        filename = "app/static/aa.jfif"

        # Save the image to a file
        with open(filename, "wb") as f:
            f.write(image_bytes)

        # Pass the filename to the Emotions_Recognition.html template
        return render_template("Emotions_Recognition.html", image_filename=filename)
    
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the API request
        return jsonify({"error": str(e)})
    
@app.route("/display_image/<filename>")
def display_image(filename):
    return send_file(filename, mimetype='image/jfif')

@app.route('/Emotions')
def Emotions():
    generated_text="sfhmaslnbazmnbakmf azkjdaizhpjagf azjkmfaihcamkf azkmhfamkfbhaozmhf "
    print("generated_text:",generated_text)
    return render_template('Emotions_Recognition.html',generated_text=generated_text)

@app.route('/Essay_correction')
def Essay_correction():
    return render_template('EssayCorrection.html')

@app.route('/Text_simplification')
def Text_simplification():
    return render_template('Text_simplification.html')

@app.route("/generate_text", methods=["POST"])
def generate_text():
    try:
        num_lines = int(request.form["num_lines"])
    except ValueError:
        return "Invalid input: num_lines must be an integer"

    upper = 0
    lower = 110
    T = []
    generated_text = ""
    result = []
    
    try:
        cv_image = request.files["image"].read()
        imgg=cv_image
        imgg = base64.b64encode(cv_image).decode("utf-8")
        nparr = np.frombuffer(cv_image, np.uint8)
        cv_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        height, width, _ = cv_image.shape
    except Exception as e:
        return f"Error processing image: {str(e)}"
    
    for i in range(num_lines):
        T.append(cv_image[upper:lower, 10:width])
        upper += 110
        lower += 110
        _, img_bytes = cv2.imencode(".jpg", T[i])
        
        response_i = {}  # Initialize response_i as an empty dictionary
        
        while not response_i:
            response_i = requests.post(API_URL_trocr, headers=headers, data=img_bytes.tobytes())
        
        result_i = response_i.json()
        result.append(result_i)
        
        if i > 0:
            generated_text += " "
        generated_text += result_i[0]['generated_text']

    # Render the HTML template with the generated_text
    return render_template("EssayCorrection.html", generated_text=generated_text, num_lines=num_lines,imgg=imgg)

@app.route("/correct_text", methods=["POST"])
def correct_text():
    user_input = request.form["user_input"]

    # Use the user_input as input for ChatGPT
    messages = [
        {
            "role": "user",
            "content": user_input
        },
        {
            "role": "assistant",
            "content": "Act like a teacher and assign a grade (A, B, C, D, E, or F) for the paragraph provided."
        },
        {
            "role": "assistant",
            "content": "Analyze the pros of the paragraph."
        },
        {
            "role": "assistant",
            "content": "Analyze the cons of the paragraph."
        }
    ]

    try:
        # Make the OpenAI chat completion request
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        assistant_reply = response.choices[0].message["content"]
        
        # Use markers to split the response into sections
        markers = ["Grade:", "Pros:", "Cons:"]
        section_contents = {}
        
        current_section = markers[0]
        for line in assistant_reply.split('\n'):
            if line in markers:
                current_section = line
            else:
                section_contents.setdefault(current_section, []).append(line)
        
        grade = "\n".join(section_contents["Grade:"])
        pros = "\n".join(section_contents["Pros:"])
        cons = "\n".join(section_contents["Cons:"])
        
        # Check if "Corrected Text:" is in the response

    except Exception as e:
        return f"Error generating assistant reply: {str(e)}"

    # Render the HTML template with the variables
    return render_template("EssayCorrection.html", grade=grade, pros=pros, cons=cons, user_input=user_input)
@app.route("/simplify", methods=["GET", "POST"])
def simplify():
    if request.method == "GET":
        return render_template("simplify.html")

   
    user_input = request.form["user_input"]
    generated_text = user_input  # Use the user-provided text as input

    # Use the generated_text as input for ChatGPT
    messages = [
        {
            "role": "system",
            "content": "Simplify the paragraph given please so a 5-year-old can understand it make it like a short story of 6 sentences add some emoji s : "
        },
        {
            "role": "user",
            "content": generated_text  # Use the user-provided text as the user's input
        }
    ]

    # Make the OpenAI chat completion request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    assistant_reply = response.choices[0].message["content"]

    return render_template("simplify.html", generated_text=generated_text, corrected_text=assistant_reply)
@app.route('/profile')
def profile():
    return render_template('profile.html')