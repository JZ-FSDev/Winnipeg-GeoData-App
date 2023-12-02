import math_utils as mu
import interactive_map as im
import access_mssql as ms
from flask import Flask, jsonify, render_template
import config_reader as cr


populated = False  # Flag to ensure database is populated only once
db_connection = None  # A connection to our db  (May choose to make a new connection each time)

app = Flask(__name__)

# Define your API routes
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({'message': f'Hello, {name}!'})

@app.route('/api/total_wfps_call_neighbourhood', methods=['GET'])
def total_wfps_call_neighbourhood():
    result = ms.total_wfps_call_neighbourhood(db_connection)
    print(result)

@app.route('/api/total_substance_neighbourhood', methods=['GET'])
def total_substance_neighbourhood():
    result = ms.total_substance_neighbourhood(db_connection)
    print(result)
    return jsonify({'message': 'Hello, World!'})

# Route for the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Add more API routes as needed


def main():
    global populated
    global db_connection

    if not populated:
        host, port = cr.get_host_port()
        db_connection = ms.connect_to_sql_server()
        ms.populate_database(db_connection)
        populated = True

    app.run(debug=True, host=host, port=port, use_reloader=False)


if __name__ == '__main__':
    main()
