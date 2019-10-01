from flask import render_template
from flask import Flask
import requests
from helpers import print_time
import json
#from . import app

app = Flask(__name__)

@app.route("/")
def index():
	try:
		response = requests.get("http://0.0.0.0:2000/tasks")
	except:
		response = None
	if response:
		response_data = response.json()
	return render_template("index.html", response_data=response_data)

@app.route("/dashboard")
def dashboard():
	time = print_time()
	return render_template("dashboard.html" , time=time )

app.run(debug=True)