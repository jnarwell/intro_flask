from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#create instance
app = Flask(__name__)
#configure app with secret key
app.config.from_object(Config)

#create instance of database 
db = SQLAlchemy(app)

#create instance of migrate to handle database migrations
migrate = Migrate(app, db)

from app import routes
#must be imported at bottom of file