from flask import *
from formsubmission import GogetRegistrationForm
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/sam_db' #/// SLASH denotaes relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#app.secret_key='private_key' #use for this encrypt/decrypt data

db=SQLAlchemy(app)

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    password=db.Column(db.String(100))

    def __init__(self,name,password):
        self.name=name
        self.password=password
db.create_all()


@app.route('/')
def defaultHome():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='post':
        username=request.form['name']
        session['name']=username
        password=request.form['password']
        session['password']=password
        found_user=User.query.filter(User.name==username and User.password==password).all()
        if found_user:
            return render_template('dashbord.html')
        else:
            if not found_user:
                return render_template('login.html')


    else:
        if request.method=='GET':
            return render_template('login.html')

@app.route('/dashbord')
def dashbord():
    list={'John':1000,'Smith':-500,'Merry':1500}
    return render_template('dashbord.html',dashbord=list)

#registration form
@app.route('/registrationform',methods=['POST','GET'])
def registrationForm():
    gogetregistrationform=GogetRegistrationForm()
    if request.method=='POST':
        if request.form['name']=='' and request.form['password']=='':
            flash("Please fill out this fields")
            if request.form['name']!='' and request.form['password']!='':
                name=request.form['name']
                password=request.form['password']
                found_user=User.query.filter(User.name==name and User.password==password).all()
                if found_user:
                    return render_template('error.html')
                else:
                    if not found_user:
                        data=User(request.form['name'],request.form['password'])
                        db.session.add(data)
                        db.session.commit()
                        return render_template('login.html')

    elif request.method=='GET':
        return render_template('register.html',form=gogetregistrationform)


@app.route('/successformsubmission')
def successformsubmission():
    name=session.get('name',None)
    return render_template('successformsubmission.html')


if __name__=='__main__':

    app.run(debug=True)