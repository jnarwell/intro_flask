from app import app
from flask import render_template

#add a route
@app.route('/')
def index():
    countries = ['China', 'India', 'Canada']
    return render_template('index.html', first_name='Jamie', countries = countries)

@app.route('/signup')
def new():
    return render_template('signup.html')