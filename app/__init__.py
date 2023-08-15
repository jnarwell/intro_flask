from flask import Flask

#create instance
app = Flask(__name__)
#configure app with secret key
app.config['SECRET_KEY'] = 'you-will-never-guess'


from app import routes
#must be imported at bottom of file