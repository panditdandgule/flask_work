from flask import Blueprint,render_template

route=Blueprint('route',__name__)

@route.route('/home')
def hme():
    return render_template('index.html')