from app import app
from flask import render_template, request
from models.list_of_events import *
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title="Home", events=events, headings=headings)


@app.route('/events', methods=['POST'])
def add_task():
    date = request.form["date"]
    name_of_event = request.form["name_of_event"]
    number_of_guests = request.form["number_of_guests"]
    room_location = request.form["room_location"]
    description = request.form["description"]
    result = request.form["recurring"]
    if result == "on":
        recurring = True
    else:
        recurring = False
    new_event = Event(date, name_of_event, number_of_guests, room_location, description, recurring)
    add_new_event(new_event)
    return render_template('index.html', title="Home", events=events, headings=headings)