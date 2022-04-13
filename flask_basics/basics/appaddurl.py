from flask import Flask

app=Flask(__name__)

def about():
    return "This is about page"

#add_url_rule(<url rule>, <endpoint>, <view function>)
app.add_url_rule("/about","about",about)

if __name__=='__main__':
    app.run(debug=True)