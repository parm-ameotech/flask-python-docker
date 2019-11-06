from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'User'
	id = db.Column(db.Integer(20),primary_key=True,autoincrement=True)
	email = db.Column(db.String(100),unique=True,nullable=False)
	password = db.Column(db.String(100),nullable=False)
	def __init__(self , email ,password):
		self.email = email
		self.password = password
		self.email = email

