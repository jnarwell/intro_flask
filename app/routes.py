from app import app, db
from flask import render_template, redirect, url_for
from app.forms import SignUpForm, PostForm
from app.models import User

# Add a route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        check_user = db.session.execute(db.select(User).where( (User.username==username) | (User.email==email) )).scalar()
        if check_user:
            print('A user with that username/password already exists')
            return redirect(url_for('signup'))
        
        #create nw instance of user class with data from form
        new_user = User(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()

        #redirect to home page
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)

@app.route('/create', methods=["GET", "POST"])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        # Get the data from the form
        title = form.title.data
        body = form.body.data
        image_url = form.image_url.data or None
        print(title, body, image_url)

        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)