from flask import render_template
from flask import Flask
import requests
import json
import os
from customers import app

@app.route("/")
def index():
	# user = User(password='password@123')
	# db.session.add(user)
	# db.session.commit
	user = User.query.filter_by(password='password@123')
	data ={
		'name':'Customer Site', 'user':user.count()
	}
	return render_template("index.html", data=data)



app.run(debug=True,host="0.0.0.0",port=5001)