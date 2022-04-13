from app import app
from config import mysql
from flask import jsonify, request, flash
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/add', methods=['POST'])
def add_user():
    conn = None
    cursor = None
    try:
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _password = _json['password']

        if _name and _email and _password and request.method == 'POST':
            _hashed_password = generate_password_hash(_password)

            # save data
            sql = "INSERT INTO users(name,email,password) values (%s,%s,%s)"
            data = (_name, _email, _hashed_password,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify("User added successfully")
            resp.status_code = 200
            return resp
        else:
            return not_found()

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run()
