import math_utils as mu
import interactive_map as im
import access_mssql as ms
from flask import Flask, jsonify
import config_reader as cr



app = Flask(__name__)

# Define your API routes
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({'message': f'Hello, {name}!'})

# Add more API routes as needed

if __name__ == '__main__':
    # Run the app locally on port 5000
    host, port = cr.get_host_port()

    app.run(debug=True, host=host, port=port)