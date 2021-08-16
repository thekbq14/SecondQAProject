from . import db

class Planner(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    city = db.Column(db.String(30), nullable=True)
    transport = db.Column(db.String(30), nullable=True)
    time = db.Column(db.float)