from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# add those later
DBHOST = os.environ.get("DBHOST")
DBPORT = os.environ.get("DBPORT")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@postgres_distribution/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print(db.session.execute('SELECT 1'))

from . import routes