from flask import request, jsonify, make_response
from models import Users, Authors, db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps
from config import app

"""This function will generate tokens in order to allow only registered users 
to access and perform a set of  API operations against the Authors table."""


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({"message": "a valid token is missing"})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = Users.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = Users(public_id=str(uuid.uuid4()),
                     name=data['name'],
                     password=hashed_password,
                     admin=False)

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "registered successfully"})


@app.route('/login', methods=['GET', 'POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response("could not verify", 401, {'WWW.Authentication': 'Basic realm: "login required"'})

    user = Users.query.filter_by(name=auth.username).first()

    if check_password_hash(user.password, auth.password):
        token = jwt.encode(
            {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'])
        return jsonify({'token': token})

    return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})


@app.route('/users', methods=['GET'])
def get_all_users():
    users = Users.query.all()

    result = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin

        result.append(user_data)

    return jsonify({"users": result})


@app.route('/author', methods=['POST', 'GET'])
@token_required
def create_author(current_user):
    data = request.get_json()

    new_authors = Authors(name=data['name'],
                          country=data['country'],
                          book=data['book'],
                          booker_prize=True,
                          user_id=current_user.id)
    db.session.add(new_authors)
    db.session.commit()

    return jsonify({'message': 'new author created'})


@app.route('/authors', methods=['GET', 'POST'])
@token_required
def get_authors(current_user):
    authors = Authors.query.filter_by(user_id=current_user.id).all()

    output = []
    for author in authors:
        author_data = {}
        author_data['name'] = author.name
        author_data['book'] = author.book
        author_data['country'] = author.country
        author_data['booker_prize'] = author.booker_prize
        output.append(author_data)

    return jsonify({'List Of Authors': output})


@app.route('/authors/<author_id>', methods=['DELETE'])
@token_required
def delete_author(current_user, author_id):
    author = Authors.query.filter_by(id=author_id, user_id=current_user.id).first()
    if not author:
        return jsonify({'message': 'author does not exist'})

    db.session.delete(author)
    db.session.commit()

    return jsonify({'message': 'Author deleted'})


if __name__ == '__main__':
    app.run(debug=True)
