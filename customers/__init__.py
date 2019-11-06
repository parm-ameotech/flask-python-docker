from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHAMY_DATABASE_URI'] =  \
	'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(
		user = os.environ.get('POSTGRES_USER'),
		password = os.environ.get('POSTGRES_PASSWORD'),
		host = os.environ.get('POSTGRES_HOST'),
		port = os.environ.get('POSTGRES_PORT'),
		db_name = os.environ.get('POSTGRES_DB'),
	)
db = SQLAlchemy(app)

from customers import models, apps
