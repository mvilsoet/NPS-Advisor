# Required to make Python treat nps-advisor as a packagefrom flask import flask
import os
import sqlalchemy
from yaml import load, Loader
from flask import Flask

#  starts a connection to the GCP database
def init_connect_engine():
    if os.environ.get('GAE_ENV') != 'standard':
        variables = load(open("app.yaml"), Loader=Loader)
        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'), #username
            password=os.environ.get('MYSQL_PASSWORD'), #user password
            database=os.environ.get('MYSQL_DB'), #database name
            host=os.environ.get('MYSQL_HOST') #ip
        )
    )
    return pool

app = Flask(__name__, template_folder='./templates', static_folder='./static')
db = init_connect_engine()
""" 
#Testing Database Connection
conn = db.connect()
results = conn.execute("Select * FROM Parks LIMIT 5;" )
print([x for x in results])
conn.close()

 """
from app import routes
