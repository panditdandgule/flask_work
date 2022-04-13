from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3305/emp_db'  # mysql connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Flask app instance --> sqlalchemy --> db configuration.
# db--> type --> SQLAlChemy --> what that object is aware --> app --> Flask instance
