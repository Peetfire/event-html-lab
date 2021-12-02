from models.event import *

event1 = Event("27/12/2021", "CodeClan Marathon", 16, "Hopper", "Coding marathon for E54", False)
event2 = Event("14/03/2022", "CodeClan Graduation", 16, "Pub", "Graduation for E54", True)
event3 = Event("02/08/2022", "CodeClan Bowling Night", 16, "Tenpin", "Bowling Championship", False)

events = [event1, event2, event3]

headings = ["Date", "Name of Event", "Number of Guests", "Room Location", "Description", "Recurring"]

def add_new_event(new_event):
    events.append(new_event)