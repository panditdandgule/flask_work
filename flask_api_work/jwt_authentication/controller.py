from config import app
from models import db, Account, Customer
import json
import time
from flask import Flask, request, jsonify
from datetime import timedelta
from flask_jwt_extended import get_jwt, JWTManager, create_access_token, create_refresh_token, jwt_required, \
    get_jwt_identity

app.config['JWT_SECRET_KEY'] = "@#$%DHFKJDSjkfhkds(*^&"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(hours=8)
jwt = JWTManager(app)
#https://www.getpostman.com/collections/6460c99942f9e097c2ba

@app.route("/customer/save", methods=['POST'])
@jwt_required()
def add_customer():
    reqdata = request.get_json()
    if not reqdata:
        return json.dumps({"ERROR": "Customer Fields Cannot blank"})
    try:
        cust = Customer.query.filter_by(id=reqdata.get('id')).first()
        if cust:
            return json.dumps({"ERROR": "Customer ID already present"})
        cust = Customer(id=reqdata.get('id'),
                        name=reqdata.get('name'),
                        username=reqdata.get('username'),
                        password=reqdata.get('password'),
                        email=reqdata.get('email'))
        print("Customer Record", cust)
        db.session.add(cust)
        db.session.commit()
        return json.dumps({"SUCCESS": "Customer Record added into databases"})
    except BaseException as e:
        print(e.args)
        return json.dumps({"ERROR": "Problem in customer add"})


def application_req():
    print('initializing the system....')

    cust1 = Customer(id=101, name='Yogesh1', username='yogymax1', password='yogy@123', email='yogesh1@gmail.com')
    cust2 = Customer(id=102, name='Yogesh2', username='yogymax2', password='yogy@123', email='yogesh2@gmail.com')
    cust3 = Customer(id=103, name='Yogesh3', username='yogymax3', password='yogy@123', email='yogesh3@gmail.com')
    db.session.add_all([cust1, cust2, cust3])
    db.session.commit()
    ac1 = Account(id=111111, balance=28693.34, type='saving', cust_id=cust1.id)
    ac2 = Account(id=111112, balance=25893.34, type='saving', cust_id=cust1.id)
    ac3 = Account(id=111113, balance=28933.34, type='saving', cust_id=cust2.id)
    ac4 = Account(id=111114, balance=28893.34, type='Current', cust_id=cust2.id)
    ac5 = Account(id=111115, balance=92893.34, type='saving', cust_id=cust3.id)
    db.session.add_all([ac1, ac2, ac3, ac4, ac5])
    db.session.commit()
    print('Objects created...')


# http://localhost:5000/api/customer/1212
@app.route('/api/customer/<int:cust_id>')
@jwt_required()
def get_customer_account_balance(cust_id):
    customer = Customer.query.filter_by(id=cust_id).first()  # .all()
    if customer:
        customer_accounts = customer.accounts  # list -
        customer_account_serializer = [
            {'customer_id': customer.id, 'customer_name': customer.name}]  # json format madhe
        for account in customer_accounts:
            account = {"ACCOUNT_NUMBER ": account.id, "ACCOUNT_TYPE": account.type, "ACCOUNT_BALANCE": account.balance}
            # "CUSTOMER_NAME":account.customer.name}
            customer_account_serializer.append(account)
        return json.dumps(customer_account_serializer)
    return json.dumps({"ERROR": "No Details found for given customer id {}".format(cust_id)})


# http://localhost:5000/api/token  {"username":"yogesh",password:"yogesh123"}
@app.route("/api/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    record = Customer.query.filter(Customer.username == username, Customer.password == password).first()
    print(record)
    if record:
        # if username=='root' and password == 'root':
        identity = (record.username, record.password)
        # identity = (username,password)
        accessToken = create_access_token(identity=identity)
        refreshToken = create_refresh_token(identity=identity)
        return jsonify({"ACCESS_TOKEN": accessToken, "REFRESH_TOKEN": refreshToken,
                        "USERNAME": username})
    else:
        return jsonify({"msg": "Bad username or password"}), 401


@app.route("/api/token/refresh", methods=["GET"])
@jwt_required(refresh=True)  # token --> refresh True -- refresh token
def get_refresh_token():
    current_user_id = get_jwt_identity()  # username,password
    accesstoken = create_access_token(identity=current_user_id)  #
    return jsonify({"accesstoken": accesstoken})


@app.route('/api/customer/')
@jwt_required()
def get_customer_details():
    customers = Customer.query.all()
    all_customers = []
    for cust in customers:
        all_customers.append({"ID": cust.id,
                              "Name": cust.name,
                              "Username": cust.username,
                              "Password": cust.password,
                              "Email": cust.email})
    print(all_customers)

    return jsonify({"Customers": all_customers})


@app.route('/api/account/')
def get_customer_account_details():
    account = Account.query.all()
    all_accDetails = []
    for acc in account:
        all_accDetails.append({
            "ID": acc.id,
            "Account Balance": acc.balance,
            "Account Type": acc.type,
            "Customer ID": acc.cust_id
        })
    return jsonify({"Account Details": all_accDetails})


@app.route('/api/customer/<int:id>')
def search_customer_by_account():
    pass


@app.route('/api/customer/<str:email>')
def search_customer_by_email():
    pass


if __name__ == '__main__':
    # application_req()
    app.run(debug=True)
