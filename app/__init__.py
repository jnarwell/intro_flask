from flask import Flask

#create instance
app = Flask(__name__)

from app import routes
#must be imported at bottom of file