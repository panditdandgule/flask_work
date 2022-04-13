from flask import Flask, render_template, request, redirect, abort
from models import db, UsersModel

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method=='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        city = request.form['city']

        users = UsersModel(
            fname=fname,
            lname=lname,
            age=age,
            city=city
        )
        db.session.add(users)
        db.session.commit()
        return redirect('/')


@app.route('/', methods=['GET'])
def retrivelist():
    users = UsersModel.query.all()
    return render_template('/', users=users)


@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def update(id):
    user = UsersModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        db.sesssion.delete(user)
        db.session.commit()

        if user:
            fname = request.form['fname']
            lname = request.form['lname']
            age = request.form['age']
            city = request.form['city']

            users = UsersModel(
                fname=fname,
                lname=lname,
                age=age,
                city=city
            )
            db.session.add(users)
            db.session.commit()
            return redirect('/')
        return f"User id with {id} does not exists"
    return render_template('update.html')


@app.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    users = UsersModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/')
        abort(404)
    return render_template('delete.html')

if __name__=='__main__':
    app.run(debug=True)