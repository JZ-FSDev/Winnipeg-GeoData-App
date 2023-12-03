import math_utils as mu
import interactive_map as im
import access_mssql as ms
from flask import Flask, jsonify, render_template
import config_reader as cr


db_connection = None  # A connection to our db  (May choose to make a new connection each time)

app = Flask(__name__)

# Define your API routes
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({'message': f'Hello, {name}!'})

@app.route('/api/total_wfps_call_neighbourhood', methods=['POST'])
def total_wfps_call_neighbourhood():
    result = ms.total_wfps_call_neighbourhood(db_connection)
    json_result = [{'neighbourhood': item[0], 'num_houses': item[1], 'call_count': item[2]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/total_substance_neighbourhood', methods=['POST'])
def total_substance_neighbourhood():
    result = ms.total_substance_neighbourhood(db_connection)
    json_result = [{'neighbourhood': item[0], 'substance_count': item[1]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/count_lane_closure_street', methods=['POST'])
def count_lane_closure_street():
    result = ms.count_lane_closure_street(db_connection)
    json_result = [{'street_name': item[0], 'street_type': item[1], 'closure_count': item[2]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/count_parking_citation_street', methods=['POST'])
def count_parking_citation_street():
    result = ms.count_parking_citation_street(db_connection)
    json_result = [{'street_name': item[0], 'street_type': item[1], 'closure_count': item[2]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/bus_route_avg_deviation', methods=['POST'])
def bus_route_avg_deviation():
    result = ms.bus_route_avg_deviation(db_connection)
    json_result = [{'route_number': item[0], 'average_deviation': item[1]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/street_paystation', methods=['POST'])
def street_paystation():
    result = ms.street_paystation(db_connection)
    json_result = [{'street_name': item[0], 'street_type': item[1], 'paystation_id': item[2], 'time_limit': item[3], 'space': item[4]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/count_tow_neighbourhood', methods=['POST'])
def count_tow_neighbourhood():
    result = ms.count_tow_neighbourhood(db_connection)
    json_result = [{'neighbourhood': item[0], 'tow_count': item[1]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/bus_stop_neighbourhood_bus_route', methods=['POST'])
def bus_stop_neighbourhood_bus_route():
    result = ms.bus_stop_neighbourhood_bus_route(db_connection)
    json_result = [{'bus_stop_number': item[0], 'longitude': item[1], 'latitude': item[2], 'neighbourhood': item[3], 'route_number': item[4], "route_destination": item[5]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/latest_wfps_neighbourhood', methods=['POST'])
def latest_wfps_neighbourhood():
    result = ms.latest_wfps_neighbourhood(db_connection)
    json_result = [{'neighbourhood': item[0], 'call_date': item[1], 'reason': item[2], 'call_time': item[3]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/count_bus_stop_street', methods=['POST'])
def count_bus_stop_street():
    result = ms.count_bus_stop_street(db_connection)
    json_result = [{'street_name': item[0], 'street_type': item[1], 'bus_count': item[2]} for item in result]
    return jsonify({'result': json_result})

# Route for the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Add more API routes as needed


def main():
    global db_connection

    host, port = cr.get_host_port()
    db_connection = ms.connect_to_sql_server()
    # ms.populate_database(db_connection)

    # app.run(debug=True, host=host, port=port, use_reloader=False)
    app.run(debug=True, host=host, port=port)

if __name__ == '__main__':
    main()
