from flask import Flask, jsonify , json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	data={
		'name':'Index',
	}
	response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    	)
	return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)