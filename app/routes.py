from app import app
from flask import render_template
from app.forms import SignUpForm

# Add a route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)