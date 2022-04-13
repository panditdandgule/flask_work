from flask import Flask
from mysite.route import route

def create_app():
    app=Flask(__name__)
    app.register_blueprint(route)
    return app