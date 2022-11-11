from flask import Flask, render_template, request, jsonify
from flask_navigation import Navigation
from app import app
from app import database as db_helper
import sys
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'homepage'),
    nav.Item('Events', 'events')
])

@app.route("/")
def homepage():
    activities = db_helper.get_activities()
    states = db_helper.get_states()
    parks = db_helper.fetch_parks()
    return render_template("index.html", activities=activities, states=states, parks=parks) # name-db_helper()

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/search", methods = ['GET', 'POST'])
def search():
    input = request.form.get('query')
    print(f"Input: {input}", file=sys.stderr)
    parks = db_helper.search_parks(input)
    activities = db_helper.get_activities()
    states = db_helper.get_states()
    return render_template("index.html", activities=activities, states=states, parks=parks)