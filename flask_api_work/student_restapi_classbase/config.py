from flask import Flask
from flask_restful import Api
from student_restapi_classbase.models import db
from student_restapi_classbase.controller import StudentRoute

app=Flask(__name__)
api=Api()
app.config['SECRET_KEY']='ajdljdskljk'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/sam_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(StudentRoute,"/student","/student/<int:id>")

if __name__=='__main__':
    db.init_app(app)
    api.init_app(app)
    app.run(debug=True,host='localhost')