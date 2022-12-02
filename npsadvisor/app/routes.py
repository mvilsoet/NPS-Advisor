from flask import Flask, request, render_template, jsonify
from flask_navigation import Navigation
from app import app
from app import database as db_helper

nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'homepage'),
    nav.Item('Events', 'events'),
    nav.Item('In Season', 'in_season'),
    nav.Item('Parking Lots', 'parking_lots')
])

@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        try:
            request.form['state'] #1: if a state code was posted...
        except:
            search_query = request.form['park'] #3: if a state wasn't posted... a park_name was, so use it
            parks = db_helper.search_parks_by_name(search_query=search_query)
        else:
            search_query = request.form['state'] #2: use it in the query
            parks = db_helper.search_parks_by_state(search_query=search_query)

        return render_template("index.html", parks=parks)
    parks = db_helper.get_parks()
    return render_template("index.html", parks=parks) # name-db_helper()

@app.route("/in_season", methods=['GET', 'POST'])
def in_season():
    if request.method == 'POST':
        input = request.form['search']
        parks = db_helper.in_season(input)
        return render_template("in_season.html", parks=parks)
    parks = db_helper.get_parks()
    return render_template("in_season.html", parks=parks) # name-db_helper()

@app.route("/parkinglots")
def parking_lots():
    parking = db_helper.get_parking()
    print(parking)
    return render_template("parking.html", markers=parking)

@app.route("/events", methods=['GET', 'POST'])
def events():
    free_parking_events = db_helper.get_events_free_parking()
    park_names = db_helper.get_parknames()
    if request.method == 'POST':
        search_query = request.form['park']
        events = db_helper.search_events(search_query=search_query)
        return render_template("events.html", park_names=park_names, events=events, free_parking=free_parking_events)
    events = db_helper.get_events()
    return render_template("events.html", park_names=park_names, events=events, free_parking=free_parking_events)

@app.route("/create_event", methods=['POST'])
def create_event():
    data = request.get_json()
    # print(data)
    db_helper.insert_new_event(data['title'], data['description'], data['start_date'], data['end_date'], data['park_name'])
    result = {'success': True, 'response': 'Done'}

    return jsonify(result)

@app.route("/delete_event", methods=['POST'])
def delete_event():
    # print(request.get_json())
    db_helper.delete_event(request.get_json()['id'])
    # free_parking_events = db_helper.get_events_free_parking()
    # park_names = db_helper.get_parknames()
    # events = db_helper.get_events()
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)#render_template("events.html", park_names=park_names, events=events, free_parking=free_parking_events)

@app.route("/edit_event", methods=['POST'])
def edit_event():
    data = request.get_json()
    # print(data)
    db_helper.edit_event(data['id'], data['title'], data['description'], data['start_date'], data['end_date'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)
