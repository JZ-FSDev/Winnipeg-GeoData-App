import interactive_map as im
import access_mssql as ms
from flask import Flask, jsonify, render_template, request
import config_reader as cr
import pandas as pd


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
    im.update_empty_map()  # Clear map
    result = ms.total_wfps_call_neighbourhood(db_connection)
    json_result = [{'neighbourhood': item[0], 'num_houses': item[1], 'call_count': item[2]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/total_substance_neighbourhood', methods=['POST'])
def total_substance_neighbourhood():
    im.update_empty_map()  # Clear map
    result = ms.total_substance_neighbourhood(db_connection)
    json_result = [{'neighbourhood': item[0], 'substance_count': item[1]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/count_lane_closure_street', methods=['POST'])
def count_lane_closure_street():
    im.update_empty_map()  # Clear map
    result = ms.count_lane_closure_street(db_connection)
    json_result = [{'street_name': item[0], 'street_type': item[1], 'closure_count': item[2]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/count_parking_citation_street', methods=['POST'])
def count_parking_citation_street():
    im.update_empty_map()  # Clear map
    result = ms.count_parking_citation_street(db_connection)
    json_result = [{'street_name': item[0], 'street_type': item[1], 'closure_count': item[2]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/bus_route_avg_deviation', methods=['POST'])
def bus_route_avg_deviation():
    im.update_empty_map()  # Clear map
    result = ms.bus_route_avg_deviation(db_connection)
    json_result = [{'route_number': item[0], 'route_destination': item[1], 'average_deviation': item[2]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/street_paystation', methods=['POST'])
def street_paystation():
    im.update_empty_map()  # Clear map
    result = ms.street_paystation(db_connection)
    json_result = [{'street_name': item[0], 'street_type': item[1], 'paystation_id': item[2], 'time_limit': item[3], 'space': item[4]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/tows_in_neighbourhood', methods=['POST'])
def tows_in_neighbourhood():
    data = request.get_json()
    neighbourhood = data.get('neighbourhood')
    
    result = ms.tows_in_neighbourhood(db_connection, neighbourhood)

    if len(result) > 0:
        columns = ['tow_id', 'Latitude', 'Longitude']
        df = pd.DataFrame(result, columns=columns)
        im.update_map(df, 'tow_id')

        json_result = [{'tow_id': item[0], 'date_from': item[1], 'date_to': item[2]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})

@app.route('/api/bus_stop_neighbourhood_bus_route', methods=['POST'])
def bus_stop_neighbourhood_bus_route():
    im.update_empty_map()  # Clear map
    result = ms.bus_stop_neighbourhood_bus_route(db_connection)
    json_result = [{'bus_stop_number': item[0], 'longitude': item[1], 'latitude': item[2], 'neighbourhood': item[3], 'route_number': item[4], "route_destination": item[5]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/latest_wfps_neighbourhood', methods=['POST'])
def latest_wfps_neighbourhood():
    im.update_empty_map()  # Clear map
    result = ms.latest_wfps_neighbourhood(db_connection)
    json_result = [{'neighbourhood': item[0], 'call_date': item[1], 'reason': item[2], 'call_time': item[3]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/count_bus_stop_street', methods=['POST'])
def count_bus_stop_street():
    im.update_empty_map()  # Clear map
    result = ms.count_bus_stop_street(db_connection)
    json_result = [{'street_name': item[0], 'street_type': item[1], 'bus_count': item[2]} for item in result]
    return jsonify({'result': json_result})

@app.route('/api/lane_closures_in_neighbourhood', methods=['POST'])
def lane_closures_in_neighbourhood():
    data = request.get_json()
    neighbourhood = data.get('neighbourhood')
    
    result = ms.lane_closures_in_neighbourhood(db_connection, neighbourhood)

    if len(result) > 0:
        columns = ['lane_closure_id', 'date_from', 'date_to', 'Latitude', 'Longitude']
        df = pd.DataFrame(result, columns=columns)
        im.update_map(df, 'lane_closure_id')

        json_result = [{'lane_closure_id': item[0], 'date_from': item[1], 'date_to': item[2]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})
    
@app.route('/api/bus_stops_on_street', methods=['POST'])
def bus_stops_on_street():
    data = request.get_json()
    street_name = data.get('street_name')
    street_type = data.get('street_type')
    num_meters = data.get('num_meters')
    
    if num_meters == '':
        num_meters = 0 

    result = ms.bus_stops_on_street(db_connection, street_name, street_type, num_meters)

    if len(result) > 0:
        columns = ['bus_stop', 'Latitude', 'Longitude']
        df = pd.DataFrame(result, columns=columns)
        im.update_map(df, 'lane_closure_id')

        json_result = [{'lane_closure_id': item[0], 'date_from': item[1], 'date_to': item[2]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})

# Route for the index.html page
@app.route('/')
def index():
    im.update_empty_map()  # Clear map
    return render_template('index.html')

# Add more API routes as needed


def main():
    global db_connection

    host, port = cr.get_host_port()
    db_connection = ms.connect_to_sql_server()
    # ms.populate_database(db_connection)

    app.run(debug=True, host=host, port=port, use_reloader=False)
    # app.run(debug=True, host=host, port=port)

if __name__ == '__main__':
    main()
