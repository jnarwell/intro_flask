from flask_httpauth import HTTPBasicAuth
from app import db
from app.models import User

basic_auth = HTTPBasicAuth()

@basic_auth.verify_password
def verify(username, password):
    print(username,password)
    user = db.session.execute(db.select(User).where(User.username==username)).scalar()
    if user is not None and user.check_password(password):
        return user
    return None

@basic_auth.error_handler
def handle_error(status):
    return {'error':'Incorrect username and/or password'}, status