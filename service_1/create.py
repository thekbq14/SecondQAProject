from application import db
from application.models import Transport

db.drop_all()
db.create_all()

db.session.add()
db.session.commit()