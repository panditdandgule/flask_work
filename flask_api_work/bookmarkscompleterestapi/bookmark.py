from flask import Blueprint

bookmark=Blueprint('bookmark',__name__)

@bookmark.route('/home')
def home_page():
    return 'Welcome Blueprint'