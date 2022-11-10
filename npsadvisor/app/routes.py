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
    return render_template("index.html", name=db_helper())

@app.route("/home")
def home():
    return render_template("index.html")

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

