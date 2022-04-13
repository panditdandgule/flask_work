from flask import Flask, request, render_template, redirect, abort
from models import UsersModel, db

app = Flask(__name__)
app.secret_key='abc'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3305/userdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('/create.html')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        city = request.form['city']

        users = UsersModel(
            name=name,
            email=email,
            password=password,
            city=city
        )
        db.session.add(users)
        db.session.commit()
        return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def retriveall():
    users = UsersModel.query.all()
    return render_template('index.html', users=users)

@app.route('/<int:id>/edit',methods=['GET','POST'])
def update(id):
    user=UsersModel.query.filter_by(id=id).first()
    if request.method=='POST':
        db.session.delete(user)
        db.session.commit()
        if user:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            city = request.form['city']

            users = UsersModel(
                name=name,
                email=email,
                password=password,
                city=city
            )
            db.session.add(users)
            db.session.commit()
            return redirect('/')
        return f'user with id={id} does not exists'
    return render_template('/update.html',user=user)


@app.route('/<int:id>/delete',methods=['GET','POST'])
def delete(id):
    user=UsersModel.query.filter_by(id=id).first()
    if request.method=='POST':
        if user:
            db.session.delete(user)
            db.session.commit()
            return redirect('/')
        abort(404)
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)
