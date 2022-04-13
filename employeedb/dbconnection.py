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
        print("There was something went wrong while connecting database",e)