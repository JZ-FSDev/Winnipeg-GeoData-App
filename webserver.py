import interactive_map as im
import access_mssql as ms
from flask import Flask, jsonify, render_template, request
import config_reader as cr
import pandas as pd
import sys


db_connection = None  # A connection to our db

app = Flask(__name__)

# Define your API routes
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({'message': f'Hello, {name}!'})

@app.route('/api/count_wfps_call_neighbourhood', methods=['POST'])
def count_wfps_call_neighbourhood():
    im.update_empty_map()  # Clear map
    result = ms.count_wfps_call_neighbourhood(db_connection)

    if len(result) > 0:
        json_result = [{'neighbourhood': item[0], 'num_houses': item[1], 'call_count': item[2]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})

@app.route('/api/count_substance_neighbourhood', methods=['POST'])
def count_substance_neighbourhood():
    im.update_empty_map()  # Clear map
    result = ms.count_substance_neighbourhood(db_connection)

    if len(result) > 0:
        json_result = [{'neighbourhood': item[0], 'num_houses': item[1], 'call_count': item[2]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})

@app.route('/api/count_lane_closure_street', methods=['POST'])
def count_lane_closure_street():
    im.update_empty_map()  # Clear map
    result = ms.count_lane_closure_street(db_connection)

    if len(result) > 0:
        json_result = [{'street_name': item[0], 'street_type': item[1], 'closure_count': item[2]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})

@app.route('/api/count_parking_citation_street', methods=['POST'])
def count_parking_citation_street():
    im.update_empty_map()  # Clear map
    result = ms.count_parking_citation_street(db_connection)
    
    if len(result) > 0:
        json_result = [{'street_name': item[0], 'street_type': item[1], 'citation_count': item[2], 'total_fines': item[3]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})

@app.route('/api/bus_route_avg_deviation', methods=['POST'])
def bus_route_avg_deviation():
    im.update_empty_map()  # Clear map
    result = ms.bus_route_avg_deviation(db_connection)

    if len(result) > 0:
        json_result = [{'route_number': item[0], 'route_destination': item[1], 'average_deviation (seconds)': item[2]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})

@app.route('/api/street_paystation', methods=['POST'])
def street_paystation():
    im.update_empty_map()  # Clear map
    result = ms.street_paystation(db_connection)

    if len(result) > 0:
        columns = ['street_name', 'street_type', 'paystation_id', 'time_limit', 'space', 'Latitude', "Longitude"]
        df = pd.DataFrame(result, columns=columns)
        im.update_map(df, 'paystation_id')

        json_result = [{'street_name': item[0], 'street_type': item[1], 'paystation_id': item[2], 'time_limit (hours)': item[3], 'space': item[4]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})
    

@app.route('/api/tows_in_neighbourhood', methods=['POST'])
def tows_in_neighbourhood():
    data = request.get_json()
    neighbourhood = data.get('neighbourhood')
    
    result = ms.tows_in_neighbourhood(db_connection, neighbourhood)

    if len(result) > 0:
        columns = ['tow_id', 'Latitude', 'Longitude', 'tow_status', 'tow_date', 'tow_time']
        df = pd.DataFrame(result, columns=columns)
        im.update_map(df, 'tow_id')

        json_result = [{'tow_id': item[0], 'tow_status': item[3], 'tow_date': item[4], 'tow_time': str(item[5])} for item in result]
        return jsonify({'result': json_result})
    else:
        im.update_empty_map()  # Clear map
        return jsonify({'result': []})

@app.route('/api/bus_route_in_neighbourhood_between_date_time', methods=['POST'])
def bus_route_in_neighbourhood_between_date_time():
    im.update_empty_map()  # Clear map
    data = request.get_json()
    start_date = data.get('start_date')
    start_time = data.get('start_time')
    end_date = data.get('end_date')
    end_time = data.get('end_time')
    neighbourhood = data.get('neighbourhood')

    result = ms.bus_route_in_neighbourhood_between_date_time(db_connection, start_date, start_time, end_date, end_time, neighbourhood)

    if len(result) > 0:
        json_result = [{'route_number': item[0], 'route_destination': item[1], 'route_name': item[2]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})

@app.route('/api/wfps_in_neighbourhood', methods=['POST'])
def wfps_in_neighbourhood():
    im.update_empty_map()  # Clear map
    data = request.get_json()
    neighbourhood = data.get('neighbourhood')

    result = ms.wfps_in_neighbourhood(db_connection, neighbourhood)
    if len(result) > 0:
        json_result = [{'wfps_call_id': item[0], 'call_date': item[1], 'reason': item[2], 'call_time': item[3]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})
    
@app.route('/api/substances_in_neighbourhood', methods=['POST'])
def substances_in_neighbourhood():
    im.update_empty_map()  # Clear map
    data = request.get_json()
    neighbourhood = data.get('neighbourhood')

    result = ms.substances_in_neighbourhood(db_connection, neighbourhood)
    if len(result) > 0:
        json_result = [{'substance_use_id': item[0], 'substance': item[1], 'date': item[2], 'time': str(item[3])} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})

@app.route('/api/count_bus_stop_street', methods=['POST'])
def count_bus_stop_street():
    im.update_empty_map()  # Clear map
    result = ms.count_bus_stop_street(db_connection)
    if len(result) > 0:
        json_result = [{'street_name': item[0], 'street_type': item[1], 'bus_count': item[2]} for item in result]
        return jsonify({'result': json_result})
    else:
        return jsonify({'result': []})

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
        im.update_empty_map()  # Clear map
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
        columns = ['bus_stop_id', 'Longitude', 'Latitude', 'date', 'scheduled_time', 'route_name']
        df = pd.DataFrame(result, columns=columns)
        im.update_map(df, 'bus_stop_id')

        json_result = [{'bus_stop_id': item[0], 'scheduled_time': str(item[4]), 'date': item[3], 'route_name': item[5]} for item in result]
        return jsonify({'result': json_result})
    else:
        im.update_empty_map()  # Clear map
        return jsonify({'result': []})
    
@app.route('/api/parking_citation_and_tow_on_street', methods=['POST'])
def parking_citation_and_tow_on_street():
    data = request.get_json()
    street_name = data.get('street_name')
    street_type = data.get('street_type')
    
    result = ms.parking_citation_and_tow_on_street(db_connection, street_name, street_type)

    if len(result) > 0:
        columns = ['citation_id', 'fine_amount', 'violation_type', 'tow_id', 'status', 'Latitude', 'Longitude']
        df = pd.DataFrame(result, columns=columns)
        im.update_map(df, ['citation_id', 'tow_id'])

        json_result = [{'citation_id': item[0], 'fine_amount': item[1], 'violation_type': item[2], 'tow_id': item[3], 'tow_status': item[4]} for item in result]
        return jsonify({'result': json_result})
    else:
        im.update_empty_map()  # Clear map
        return jsonify({'result': []})
    
@app.route('/api/transit_delay_due_to_tow', methods=['POST'])
def transit_delay_due_to_tow():

    result = ms.transit_delay_due_to_tow(db_connection)
    if len(result) > 0:
        columns = ['bus_Latitude', 'bus_Longitude', 'scheduled_time', 'deviation (seconds)', 'route_destination', 'route_number', 'tow_Latitude', 'tow_Longitude', 'route_name', 'tow_id', 'bus_stop_id']

        df = pd.DataFrame(result, columns=columns)
        im.update_map(df, ['bus_stop_id', 'tow_id'], dual_markers=True)

        json_result = [{'scheduled_time': str(item[2]), 'deviation': item[3], 'route_destination': item[4], 'route_number': item[5], 'route_name': item[8], 'tow_id': item[9], 'bus_stop_id': item[10]} for item in result]
        return jsonify({'result': json_result})
    else:
        im.update_empty_map()  # Clear map
        return jsonify({'result': []})

@app.route('/api/transit_delay_due_to_citation', methods=['POST'])
def transit_delay_due_to_citation():

    result = ms.transit_delay_due_to_citation(db_connection)
    if len(result) > 0:
        columns = ['bus_Latitude', 'bus_Longitude', 'scheduled_time', 'deviation (seconds)', 'route_destination', 'route_number', 'citation_Latitude', 'citation_Longitude', 'route_name', 'citation_id', 'bus_stop_id']

        df = pd.DataFrame(result, columns=columns)
        im.update_map(df, ['bus_stop_id', 'citation_id'], dual_markers=True)

        json_result = [{'scheduled_time': str(item[2]), 'deviation': item[3], 'route_destination': item[4], 'route_number': item[5], 'route_name': item[8], 'citation_id': item[9], 'bus_stop_id': item[10]} for item in result]
        return jsonify({'result': json_result})
    else:
        im.update_empty_map()  # Clear map
        return jsonify({'result': []})
    
@app.route('/api/tows_due_to_lane_closures', methods=['POST'])
def tows_due_to_lane_closures():
    data = request.get_json()
    start_date = data.get('start_date')
    start_time = data.get('start_time')
    end_date = data.get('end_date')
    end_time = data.get('end_time')
    num_meters = data.get('num_meters')

    result = ms.tows_due_to_lane_closures(db_connection, num_meters, start_date, end_date, start_time, end_time)
    if len(result) > 0:
        columns = ['tow_id', 'tow_Latitude', 'tow_Longitude', 'tow_date', 'lane_Latitude', 'lane_Longitude', 'lane_closure_id', 'lane_closure_from', 'lane_closure_to']

        df = pd.DataFrame(result, columns=columns)
        im.update_map(df, ['tow_id', 'lane_closure_id'], dual_markers=True)

        json_result = [{'tow_id': item[0], 'tow_date': item[3], 'lane_closure_id': item[6], 'lane_closure_from': item[7], 'lane_closure_to': item[8]} for item in result]
        return jsonify({'result': json_result})
    else:
        im.update_empty_map()  # Clear map
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

    if len(sys.argv) > 1 and sys.argv[1] == '-populate':
        ms.populate_database(db_connection)

    app.run(debug=True, host=host, port=port, use_reloader=False)
    

if __name__ == '__main__':
    main()
