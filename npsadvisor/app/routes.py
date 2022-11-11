from flask import Flask, render_template
from flask_navigation import Navigation
from app import app
from app import database as db_helper

nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'homepage'),
    nav.Item('Events', 'events')
])

@app.route("/")
def homepage():
    parks = db_helper.test_fetch()
    return render_template("index.html", parks=parks) # name-db_helper()

@app.route("/events")
def events():
    park_names = db_helper.get_parknames()
    print(park_names)
    return render_template("events.html", park_names=park_names)

@app.route("/create_event", methods=['POST'])
def create_event():
    data = request.get_json()
    # db_helper.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)