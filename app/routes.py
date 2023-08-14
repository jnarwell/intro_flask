from app import app

#add a route
@app.route('/')
def index():
    return 'Hello World'

@app.route('/new')
def new():
    return f'This is a new route'