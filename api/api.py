from flask import Flask, jsonify , json
from flask_restplus import Api, Resource
import os
from os import environ
app = Flask(__name__)                  
api = Api(app)  

ACCESS_KEY = os.environ.get('access_key')

app.config['SECRET_KEY'] = ACCESS_KEY
ns = api.namespace('home', description='Neural')

@ns.route('/')                   
class Home(Resource):  
	def get(self):
		return {'index': 'page', 'ACCESS_KEY': ACCESS_KEY}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)