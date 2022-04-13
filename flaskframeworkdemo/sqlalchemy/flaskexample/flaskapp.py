from flask import Flask,request,render_template

#app=Flask(__name__,template_folder)
app=Flask(__name__)


@app.route('/')
def my_amazing_function():
    return "Hi Everybody"

@app.route('/homepage')
def home_my_home_page():
    return render_template("my_webpage.html")

@app.route('/home')
def home():
    my_variable="This is a variable"
    return render_template('home.html',my_variable=my_variable)

@app.route('/pandit')
def pandit():
    return render_template('biolplate.html')




if __name__=='__main__':
    app.run(debug=True,port=5000)