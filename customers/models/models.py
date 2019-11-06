from customers import db
import uuid
import datetime
from sqlalchemy import Column, Integer, Text

class User(db.Model):
	__tablename__ = 'User'
	id = db.Column(db.Integer(20),primary_key=True)
	email = db.Column(db.String(100),unique=True,nullable=False)
	password = db.Column(db.String(100),nullable=False)

	def __str__(self):
        return self.id

