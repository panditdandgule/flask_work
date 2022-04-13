from flask import *
from forms import StudentForm
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/sam_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='abc'

db=SQLAlchemy(app)

@app.route('/registeration',methods=['GET','POST'])
def registration():
    studregistrationform=StudentForm()
    if request.method=='POST':
        session['name']=request.form['name']
        if studregistrationform.validate()==False:
            flash("All Fields are required")
            return render_template('register.html',form=studregistrationform)
        else:
            return redirect(url_for('success'))
    elif request.method=='GET':
        return render_template('register.html',form=studregistrationform)

@app.route('/success')
def success():
    name=session.get('name',None)
    return render_template('success.html')



if __name__=='__main__':
    app.run(debug=True)