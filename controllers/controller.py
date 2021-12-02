from app import app
from models.list_of_events import *
from models.event import Event

@app.route('/events')
def index():
    return "Changed"