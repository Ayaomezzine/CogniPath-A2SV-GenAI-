<h1 align="center" id="title">CogniPath</h1>

<p align="center"><img src="https://socialify.git.ci/Azizomezine/CogniPath-A2SV/image?description=1&amp;descriptionEditable=CogniPath%20is%20a%20versatile%20and%20inclusive%20educational%20platform%20%20designed%20to%20support%20students%20of%20all%20backgrounds%20and%20abilities%20in%20their%20%20journey.%20&amp;font=Inter&amp;name=1&amp;pattern=Plus&amp;theme=Light" alt="project-image"></p>
<h2>Project Screenshots:</h2>

<h3>Login:</h3>



https://github.com/Me710/CogniPath-A2SV-GenAI/assets/80254112/911d4a02-3ef1-4eef-a223-8ee7d8b5de37



<h3>The home page:</h3>
<img src="https://github.com/Me710/CogniPath-A2SV-GenAI/assets/80206931/f61b7e7d-4359-4b73-a9fc-9d9e70f80ca8" alt="project-screenshot" width=auto height="auto">



 


https://github.com/Me710/CogniPath-A2SV-GenAI/assets/80254112/46177758-bd72-4f2b-bbac-0271f689cef7








<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Personalized Chatbot
*   Essay Correction
*   Emotion Recognition
*   Text Simplification
*   Health Quiz

<h2>🛠️ Installation Steps:</h2>

<p>1. Create a Virtual Environment</p>

```
python -m venv .venv
```

<p>2. Activate the Virtual Environment</p>

```
.venv\Scripts\activate
```

<p>3. Install Dependencies</p>

```
pip install -r requirements.txt
```

<p>4. Run the Application</p>

```
flask run --host=0.0.0.0 --port=5015
```
```
  |-- apps/
|    |
|    |-- home/                           # A simple app that serves HTML files
|    |    |-- routes.py                  # Define app routes
|    |
|    |-- authentication/                 # Handles auth routes (login and register)
|    |    |-- routes.py                  # Define authentication routes  
|    |    |-- models.py                  # Defines models  
|    |    |-- forms.py                   # Define auth forms (login and register) 
|    |
|    |-- static/
|    |    |-- <css, JS, images>          # CSS files, Javascript files
|    |
|    |-- templates/                      # Templates used to render pages
|    |    |-- includes/                  # HTML chunks and components
|    |    |    |-- navigation.html       # Top menu component
|    |    |    |-- sidebar.html          # Sidebar component
|    |    |    |-- footer.html           # App Footer
|    |    |    |-- scripts.html          # Scripts common to all pages
|    |    |
|    |    |-- layouts/                   # Master pages
|    |    |    |-- base-fullscreen.html  # Used by Authentication pages
|    |    |    |-- base.html             # Used by common pages
|    |    |
|    |    |-- accounts/                  # Authentication pages
|    |    |    |-- login.html            # Login page
|    |    |    |-- register.html         # Register page
|    |    |
|    |    |-- home/                      # UI Kit Pages
|    |         |-- index.html            # Index page
|    |         |-- 404-page.html         # 404 page
|    |         |-- *.html                # All other pages
|    
|  config.py                             # Set up the app
|  __init__.py                         # Initialize the app
|
|-- requirements.txt                     # App Dependencies
|
|-- .env                                 # Inject Configuration via Environment
|-- run.py                               # Start the app - WSGI gateway
|
|-- **********************************************************************
```
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Flask
*   Jinja2
*   OpenAI API (GPT-3.5 Turbo)
*   Microsoft Trocr (Optical Character Recognition)
*   OpenCV-Python
