from flask import Flask, render_template
from flask_navigation import Navigation
from app import app
from app import database as db_helper

nav = Navigation(app)



nav.Bar('top', [
    nav.Item('Home', 'home'),
    nav.Item('Things to Do', 'thingstodo'),
    nav.Item('Amenities', 'amenities'),
    nav.Item('Events', 'events'),
    nav.Item('Parking', 'parking'),
])

@app.route("/")
def homepage():
    activities = db_helper.get_activities()
    states = db_helper.get_states()
    return render_template("index.html", activities=activities, states=states)

@app.route("/home")
def home():
    activities = db_helper.get_activities()
    states = db_helper.get_states()
    return render_template("index.html", activities=activities, states=states)

@app.route('/thingstodo')
def thingstodo():
    return render_template('html/thingstodo.html')

@app.route('/amenities')
def amenities():
    return render_template('html/amenities.html')

@app.route('/events')
def events():
    return render_template('html/events.html')

@app.route('/parking')
def parking():
    return render_template('html/parking.html')

