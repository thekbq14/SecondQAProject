from . import app, db
from .models import Planner

from datetime import datetime

import requests

from sqlalchemy.sql import func

from flask import redirect, url_for

@app.route("/")
def home():

    result = "<h1>My QA Project - Transport App</h1><br>"

    city = requests.get('http://service-2:5000/get/city').text
    transport = requests.get('http://service-3:5000/get/transport').text

    journey = {'city':city, 'transport':transport}
    time = requests.post('http://service-4:5000/post/order', json=journey).json()

    record = Planner.query.order_by(Planner.id.desc()).limit(3).all()

    planner = Planner(city=city transport=transport time=time)
    db.session.add(planner)
    db.session.commit()

    return render_template("index.html", planner=planner, record=record)

