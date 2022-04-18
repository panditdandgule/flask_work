from flask import Blueprint,request,jsonify
import validators
from werkzeug.security import check_password_hash,generate_password_hash
from models import User,Bookmark,db

from flask_jwt_extended import jwt_required,get_jwt_identity,create_refresh_token,create_access_token


auth=Blueprint('auth',__name__,url_prefix='/api/v1/auth')

@auth.post('/register')
def register():
    name=request.json['name']
    email=request.json['email']
    password=request.json['password']

    if len(password) < 6:
        return jsonify({'error': "Password is too short"})

    if len(name) < 3:
        return jsonify({'error': "User is too short"})

    if not name.isalnum() or " " in name:
        return jsonify({'error': "Username should be alphanumeric, also no spaces"})

    if not validators.email(email):
        return jsonify({'error': "Email is not valid"})

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error':'Email is Taken'})

    if User.query.filter_by(name=name).first() is not None:
        return jsonify({'error':'Username is taken'})

    pwd_hash=generate_password_hash(password)

    user=User(name=name,email=email,password=pwd_hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': "User created",
        'user': {
            'name': name, "email": email
        }

    })

@auth.get('/login')
def login():
    email=request.json.get('email','')
    password=request.json.get('password','')

    user=User.query.filter_by(email=email).first()

    if user:
        is_pass_correct=check_password_hash(User.password,password)

        if is_pass_correct:
            refresh=create_refresh_token(identity=user.id)
            access=create_access_token(identity=user.id)

            return jsonify({
                'user': {
                    'refresh': refresh,
                    'access': access,
                    'username': user.name,
                    'email': user.email
                }

            })
        return jsonify({'error': 'Wrong credentials'})

@auth.get('/token/refresh')
@jwt_required(refresh=True)
def refresh_user_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({
        'access': access
    })
