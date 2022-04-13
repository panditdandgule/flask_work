from dbconnection import get_connection
import pymysql
from flask import *

app = Flask(__name__)
app.secret_key = 'pandit'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/error')
def error():
    return render_template('error.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        session['email'] = request.form['email']

    if password == 'jtp':
        resp = make_response(render_template('success.html'))
        resp.set_cookie('email', email)
        return resp
    else:
        return redirect(url_for('error'))


@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('profile.html', name=email)
    else:
        return '<p>Please login first</p>' + render_template('login.html')


@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
        return render_template('logout.html')
    else:

        return '<p>User already logged out. Please Login</p>' + render_template('login.html')


@app.route('/add', methods=["POST","GET"])
def add():
    try:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            address = request.form['address']
            conn = get_connection()
            with conn as con:
                cursor = con.cursor()
                query = "INSERT into employees (name,email,address) values('%s','%s','%s')";
                cursor.execute(query % (name, email, address))

                conn.commit()
                msg = "Employee Successfully Added in Database.."
    except pymysql.DatabaseError as e:
        if conn:
            conn.rollback()
        msg = "We can not add the employee to the database"
    finally:
        return render_template("success.html")
        con.close()
    return render_template('add.html',msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
