from flask import *

app = Flask(__name__)
app.secret_key = 'pandit'


@app.route('/error')
def error():
    return "<p><strong>Enter correct password</strong></p>"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']

    if password == 'jtp':
        rsp = make_response(render_template('success.html'))
        rsp.set_cookie('email', email)
        return rsp
    else:
        return redirect(url_for('error'))


@app.route('/viewprofile')
def profile():
    email = request.cookies.get('email')
    resp = make_response(render_template('profile.html', name=email))
    return resp

if __name__=='__main__':
    app.run(debug=True)