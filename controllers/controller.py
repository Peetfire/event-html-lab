from app import app

@app.route('/events')
def index():
    return "Changed"