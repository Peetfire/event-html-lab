from app import app
from flask import render_template
from models.list_of_events import *
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title="Home", events=events, headings=headings)