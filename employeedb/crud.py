import pymysql
from flask import *
from dbconnection import get_connection

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            address = request.form["address"]
            conn = get_connection()
            with conn as con:
                cursor = con.cursor()
                query = "INSERT into employees (name,email,address) values('%s','%s','%s')";
                cursor.execute(query % (name, email, address))

                conn.commit()
                msg = "Employee Successfully Added in Database.."
        except pymysql.DatabaseError as e:
            if conn:
                conn.rollback()
            msg = "We can not add the employee to the database"
        finally:
            return render_template("success.html", msg=msg)
            con.close()


@app.route("/view")
def view():
    conn = get_connection()
    cursor = conn.cursor()
    query="Select *from employees";
    cursor.execute(query)
    rows = cursor.fetchall()
    return render_template("view.html", rows=rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    conn = get_connection()
    with conn as con:
        try:
            cursor = con.cursor()
            query = "delete from employees where id=%d"
            print(query)
            cursor.execute(query %(id))
            con.commit()
            msg = "Record successfully deleted"
        except pymysql.DatabaseError as e:
            if con:
                con.rollback()
            msg = "Can't be deleted"
            print("Something went wrong while deleting..", e)

        finally:

            return render_template("delete_record.html", msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
