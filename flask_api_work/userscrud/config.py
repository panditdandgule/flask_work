from app import app
from flaskext.mysql import MySQL

mysql=MySQL()

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_PORT']=3305
app.config['MYSQL_DATABASE_DB']='cruddb'

mysql.init_app(app)