from app import app
from db import db

# we create the db and tables inside here before any requests will be made
@app.before_first_request
def create_all():
    db.create_all()
    