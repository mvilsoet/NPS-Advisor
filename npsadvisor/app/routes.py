from flask import Flask, render_template
# from flask_navigation import Navigation
from app import app
from app import database as db_helper

@app.route("/")
def homepage():
    parks = db_helper.fetch_parks()
    return render_template("index.html", parks=parks) # name-db_helper()