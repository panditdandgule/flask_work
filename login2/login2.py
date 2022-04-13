from flask import *

app=Flask(__name__)
app.secret_key='pandit'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['pass']
        session['email']=request.form['email']
    if password=='jtp':
        resp=make_response(render_template('success.html'))
        resp.set_cookie('email',email)
        return resp
    else:
        return redirect(url_for('error'))

@app.route('/profile')
def profile():
    if 'email' in session:
        email=request.cookies.get('email')
        resp=make_response(render_template('profile.html',name=email))
        return resp
    else:
        return '<p>Please login first</p>'

@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email',None)
        return render_template('logout.html')
    else:
        return '<p>User already logged out</p>'



if __name__=='__main__':
    app.run(debug=True)