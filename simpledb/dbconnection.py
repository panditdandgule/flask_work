import pymysql

def get_connection():
    try:
        connection=pymysql.connect(host='localhost',
                                   user='root',
                                   password='root',
                                   port=3305,
                                   database='employeedb')
        return connection
    except pymysql.DatabaseError as e:
        if connection:
            connection.rollback()
        connection.close()
        print("While connection something went wrong")

get_connection()
