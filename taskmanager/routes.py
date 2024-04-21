from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")

# Ensure that the creation of all tables is within the application context
with app.app_context():
    # Create all tables
    db.create_all()