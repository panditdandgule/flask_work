from flask import Flask,render_template,request,redirect,abort
from .models import db,StudentModel

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)


@app.before_first_request
def create_table():
	db.create_all()
	
@app.route('/create',methods=['GET','POST'])
def create():
	if request.method=='GET':
		return render_template('create.html')
		
	if request.method=='POST':
		hobby=request.form.getlist('hobbies')
		hobbies=','.join(str,hobby)
		first_name=request.form['first_name']
		last_name=request.form['last_name']
		email=request.form['email']
		password=request.form['password']
		gender=request.form['gender']
		hobbies=hobbies
		country=country.form['country']
		
		students=StudentModel(
		first_name=first_name,
		last_name=last_name,
		email=email,
		password=password,
		gender=gender,
		hobbies=hobbies,
		country=country
		)
		db.session.add(students)
		db.session.commit()
		return redirect('/')
		
@app.route('/',methods=['GET'])
def RetriveList():
	students=StudentModel.query.all()
	return render_template('index.html',students=students)
	
@app.route('/<int:id>/edit',methods=['GET','POST'])
def update(id):
	student=StudentModel.query.filter_by(id=id).first()
	
	if request.method=='POST':
		db.session.delete(student)
		db.session.commit()
		if student:
			hobby=request.form.getlist('hobbies')
			hobbies=','.join(str,hobby)
			first_name=request.form['first_name']
			last_name=request.form['last_name']
			email=request.form['email']
			password=request.form['password']
			gender=request.form['gender']
			hobbies=hobbies
			country=country.form['country']
			
			student=StudentModel(
			first_name=first_name,
			last_name=last_name,
			email=email,
			password=password,
			gender=gender,
			hobbies=hobbies,
			country=country
			)
			db.session.add(student)
			db.session.commit()
			return redirect('/')
		return f"student with id={id} does not exist"
			
	return render_template('update.html',student=student)
		
	
@app.route('/<int:id>/delete',methods=['GET','POST'])
def delete(id):
	students=StudentModel.query.filter_by(id=id).first()
	if request.method=='POST':
		if students:
			db.session.delete(students)
			db.session.commit()
			return redirect('/')
		abort(404)
	
	return render_template('delete.html')
	


if __name__=='__main__':
	app.run(debug=True)
	
