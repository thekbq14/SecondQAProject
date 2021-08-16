from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@35.242.178.92/project2")

db = SQLAlchemy(app)

from . import routes