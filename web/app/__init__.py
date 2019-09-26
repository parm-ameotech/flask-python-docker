from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# add those later
DBHOST = os.environ.get("DBHOST")
DBPORT = os.environ.get("DBPORT")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DBNAME = "postgres" #for now

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{}:{}@{}:{}/{}".format(POSTGRES_USER, POSTGRES_PASSWORD, DBHOST, DBPORT, DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print(db.session.execute('SELECT 1'))

from . import routes