<h1 align="center" id="title">CogniPath</h1>
<h2>Home page:</h2>

<img src="https://github.com/Me710/CogniPath-A2SV-GenAI/assets/80206931/f61b7e7d-4359-4b73-a9fc-9d9e70f80ca8" alt="project-screenshot" width=auto height="auto">

<h2>🧐 Structure</h2>

Here're some of the project's best features:
```
|-- .venv/                                 # Virtual environment folder
|-- requirements.txt                      # App Dependencies
|-- run.py                                # Start the app - WSGI gateway
|
|-- app/
|    |
|    |-- authentication/
|    |    |
|    |    |-- static/
|    |    |    |
|    |    |    |-- auth/
|    |    |    |    |-- css/
|    |    |    |    |-- img/
|    |    |    |    |-- js/
|    |    |    |
|    |    |    |-- front/
|    |    |    |    |-- css/
|    |    |    |    |-- img/
|    |    |    |    |-- js/
|    |    |    |-- back/
|    |    |    |    |-- css/
|    |    |    |    |-- img/
|    |    |    |    |--js/
|    |-- templates/                      # Templates used to render pages
|    |    |
|    |    |-- *.html                   # All HTML files
|    |
|    |-- views.py                       # App views and routes

```

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


  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Flask
*   Jinja2
*   OpenAI API (GPT-3.5 Turbo)
*   Microsoft Trocr (Optical Character Recognition)
*   OpenCV-Python
