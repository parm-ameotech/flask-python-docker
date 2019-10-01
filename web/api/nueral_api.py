from flask import Flask, jsonify , json
from helpers import print_time
app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_tasks():
	tasks={
		'name':'star10',
		'time':print_time()
	}
	response = app.response_class(
        response=json.dumps(tasks),
        status=200,
        mimetype='application/json'
    	)
	return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)