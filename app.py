from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"


# This is a domain name 
@app.route('/hello')
def hello():
    return "This is a hello statement -- no purpose"


@app.route('/basic')
def basic():
    return render_template(template.html)



