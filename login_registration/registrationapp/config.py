<<<<<<< HEAD
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/regdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

=======
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/regdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

>>>>>>> origin/master
db=SQLAlchemy(app)