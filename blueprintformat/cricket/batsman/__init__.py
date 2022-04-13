from flask import Blueprint,render_template

batsman=Blueprint('batsman',__name__)

@batsman.route('/batsman')
def bats():
    return render_template('batsman.html')