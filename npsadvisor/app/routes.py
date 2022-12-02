from flask import Flask, request, render_template, jsonify
from flask_navigation import Navigation
from app import app
from app import database as db_helper

nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'homepage'),
    nav.Item('Events', 'events'),
    nav.Item('Activities', 'activities'),
    nav.Item('Amenities', 'amenities'),
    nav.Item('Parking Lots', 'parking_lots'),
    nav.Item('In Season', 'in_season')
])

@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        state=request.form['state']
        park_name=request.form['park_name']
        parks= db_helper.search_parks(park_name, state)
        return render_template("index.html", parks=parks)
    parks = db_helper.get_parks()
    return render_template("index.html", parks=parks)

@app.route("/activities", methods=['GET', 'POST'])
def activities():
    if request.method == 'POST':
        try:
            request.form['state'] #1: if a state code was posted...
        except:
            try:
                request.form['season']
            except:
                search_query = request.form['name'] #3: if a state wasn't posted... a park_name was, so use it
                activity= db_helper.activities_by_name(search_query=search_query)
            else:
                search_query = request.form['season'] #3: if a state wasn't posted... a park_name was, so use it
                activity = db_helper.activities_by_season(search_query=search_query)
        else:
            search_query = request.form['state'] #2: use it in the query
            activity = db_helper.activities_by_state(search_query=search_query)

        return render_template("activities.html", activities=activity)
    activity = db_helper.get_activities()
    return render_template("activities.html", activities=activity) # name-db_helper()

@app.route("/in_season", methods=['GET', 'POST'])
def in_season():
    if request.method == 'POST':

        search_query = request.form['activities'] 
        parks = db_helper.in_season_activities(input=search_query)

        return render_template("in_season.html", parks=parks)
    parks = db_helper.get_parks()
    return render_template("in_season.html", parks=parks) # name-db_helper()

@app.route("/parkinglots")
def parking_lots():
    parking = db_helper.get_parking()
    return render_template("parking.html", markers=parking)

@app.route("/amenities", methods=['GET', 'POST'])
def amenities():
    if request.method == 'POST':

        search_query = request.form['name'] 
        amenities = db_helper.amenities_by_park(search_query=search_query)

        return render_template("amenities.html", amenity=amenities)
    amenities = db_helper.get_amenities()
    return render_template("amenities.html", amenity=amenities) # name-db_helper()

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
    db_helper.insert_new_event(data['title'], data['description'], data['start_date'], data['end_date'], data['park_name'])
    result = {'success': True, 'response': 'Done'}

    return jsonify(result)

@app.route("/delete_event", methods=['POST'])
def delete_event():
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

@app.route("/update_events", methods=['POST'])
def update_events():
    db_helper.update_events_from_api()
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/diggity_dawg", methods=['POST'])
def diggity_dawg():
    db_helper.diggity_dawg()
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)