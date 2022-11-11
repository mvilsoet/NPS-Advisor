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
    return render_template("events.html")