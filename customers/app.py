from flask import render_template
from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
	data = {
		'name': "index"
	}
	return render_template("index.html", data=data)

app.run(debug=True,host="0.0.0.0",port=5001)