from flask import Flask, request, render_template, jsonify
from flask_navigation import Navigation
from app import app
from app import database as db_helper

nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'homepage'),
    nav.Item('Events', 'events')
])

@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        search_query = request.form['park']
        parks = db_helper.search_parks(search_query=search_query)
        return render_template("index.html", parks=parks)
    parks = db_helper.get_parks()
    return render_template("index.html", parks=parks) # name-db_helper()

@app.route("/events")
def events():
    events = db_helper.get_events()
    #free_parking_events = db_helper.get_events_free_parking()
    free_parking_events = []
    park_names = db_helper.get_parknames()
    return render_template("events.html", park_names=park_names, events=events, free_parking=free_parking_events)

@app.route("/create_event", methods=['POST'])
def create_event():
    data = request.get_json()
    print(data)
    # db_helper.insert_new_event(data['title'], data['description'], data['start_date'], data['end_date'], data['park_name'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)