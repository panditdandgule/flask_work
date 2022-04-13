from config import app
from flask import render_template,request,redirect,session,url_for
from models import Users
from config import db

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'email' in session:
        return render_template('home.html')
    else:
        return redirect('/')


@app.route('/loginvalidation',methods=['POST','GET'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    users=Users.query.filter(Users.email==email, Users.password==password).first()

    if users:
        session['email']=users.email
        return redirect(url_for('home'))
    else:
        return redirect('/')

@app.route('/adduser',methods=['POST'])
def add_user():
    if request.method=='POST':
        name=request.form.get('names')
        email=request.form.get('emails')
        password=request.form.get('passwords')

        users=Users(name=name,
                    email=email,
                    password=password)
        db.session.add(users)
        db.session.commit()
        msg='User {} registered successfully'.format(users.email)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email')
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True,host='localhost',port=5000)