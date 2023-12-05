import pymssql
import config_reader as cr
import math_utils as mu

script_file = "script.sql"  # Script to generate our tables
street_file = "Street.sql"  # Script to insert Street info
neighbourhood_file = "Neighbourhood.sql"  # Script to insert Neighbourhood info
neighbourhood_street_file = "Neighbourhood_street.sql"  # Script to insert Neighbourhood_steet info
substance_file = "Substances.sql"  # Script to insert Substance info
wfps_call_file = "WFPS_Call.sql"  # Script to insert WFPS Call part 1 info
gps_point_file_address = "GPS_Point_Addresses.sql"
gps_point_file_bus_stop = "GPS_Point_Bus_Stop.sql"
gps_point_file_lane_closure = "GPS_Point_Lane_Closure.sql"
gps_point_park_citation = "GPS_Point_Park_Citation.sql"
gps_point_file_paystation = "GPS_Point_Paystation.sql"
gps_point_tow = "GPS_Point_Tow.sql"
parking_violation_file = "Parking_Violation.sql"
paystation_file = "Paystation.sql"
parking_citation_file = "Parking_Citation.sql"
lane_closure_file = "Lane_Closure.sql"
tow_file = "Tow.sql"
bus_route_file = "Bus_Route.sql"
bus_stop_file = "Bus_Stop.sql"


### Consider using multi threaded insert and transactions for the insert ###


def connect_to_sql_server():
    # Read database credentials from a configuration file
    username, password = cr.get_username_password()

    # Define the connection string with the default database and schema
    server = 'uranium.cs.umanitoba.ca'
    database = 'cs3380'
    connection_string = {
        'host': server,
        'user': username,
        'password': password,
        'database': database,
    }

    # Connect to the database
    try:
        connection = pymssql.connect(**connection_string)
        print("Connected to MSSQL server successfully")
        return connection
    except pymssql.Error as e:
        print(f"Error connecting to the database: {e}")
        exit(1)



# Populates the database by executing the sql script on the MSSQL server
def populate_database(connection):

    # Read and execute the SQL script to populate the database
    try:
        cursor = connection.cursor()

        # with open(script_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Script executed successfully.")

        # with open(street_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Streets inserted successfully.")

        # with open(neighbourhood_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Neighbourhoods inserted successfully.")

        # with open(neighbourhood_street_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Neighbourhood_Streets inserted successfully.")

        # with open(substance_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Substances inserted successfully.")

        # with open(wfps_call_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("WFPS_Calls inserted successfully.")

        # with open(gps_point_file_address) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point addresses inserted successfully.")

        # with open(gps_point_file_bus_stop) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point bus stops inserted successfully.")

        # with open(gps_point_park_citation) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point parking citations inserted successfully.")

        # with open(gps_point_file_paystation) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point paystations inserted successfully.")

        with open(gps_point_file_lane_closure) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("GPS_Point lane closures inserted successfully.")

        # with open(gps_point_tow) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point tows inserted successfully.")        

        # with open(paystation_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Paystations inserted successfully.")

        # with open(parking_violation_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Parking_Violations inserted successfully.")

        # with open(parking_citation_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Parking_Citations inserted successfully.")                            

        # with open(lane_closure_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Lane_Closures inserted successfully.")        

        # with open(tow_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Tows inserted successfully.")  

        # with open(bus_route_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Bus_Routes inserted successfully.")  

        with open(bus_stop_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Bus_Stops inserted successfully.")  

        print("All data inserted successfully")
    except FileNotFoundError:
        print(f"Could not find the script file: {script_file}")
    except pymssql.Error as e:
        print(f"Error executing the script: {e}")


# Executes the given query on via the given connection and returns the result set
def execute_query(connection, query, args=None):
    try:
        cursor = connection.cursor()
        
        if args:
            cursor.execute(query, args)
        else:
            cursor.execute(query)

        rows = cursor.fetchall()
        return rows

    except pymssql.Error as e:
        connection.close()
        print(f"Error executing the query: {e}")

    finally:
        # Close the cursor
        cursor.close() 


# Freezes due to too many WFPS Calls
# Retrieve Neighbourhood names along with the total number of houses and the count of WFPS calls for each Neighbourhood, ordered by Neighbourhood name
def total_wfps_call_neighbourhood(connection):
    query = '''
        SELECT
            n.Neighbourhood_Name,
            n.Number_OF_Houses,
            COUNT(w.WFPS_Call_ID) AS Call_Count
        FROM
            Neighbourhood n
            LEFT JOIN WFPS_Call w ON n.Neighbourhood_Name = w.Neighbourhood_Name
        GROUP BY
            n.Neighbourhood_Name, n.Number_OF_Houses
        ORDER BY
            n.Neighbourhood_Name;
    '''

    return execute_query(connection, query)


# List all Streets along with the count of Parking Citations for each street, ordered by the street name
def count_parking_citation_street(connection):
    query = '''
        SELECT
            s.Street_Name,
            s.Street_Type,
            COUNT(pc.Citation_ID) AS Citation_Count
        FROM
            Street s
            LEFT JOIN GPS_Point gp ON s.Street_Name = gp.Street_Name AND s.Street_Type = gp.Street_Type
            LEFT JOIN Parking_Citation pc ON gp.Longitude = pc.Longitude AND gp.Latitude = pc.Latitude
        GROUP BY
            s.Street_Name, s.Street_Type
        ORDER BY
            s.Street_Name;
    '''

    return execute_query(connection, query)


# Retrieve the Bus Routes along with the average deviation for each route, ordered by route number
def bus_route_avg_deviation(connection):
    query = '''
        SELECT
            br.Route_Number,
            AVG(bs.Deviation) AS Average_Deviation
        FROM
            Bus_Route br
            LEFT JOIN Bus_Stop bs ON br.Route_Number = bs.Route_Number AND br.Route_Destination = bs.Route_Destination
        GROUP BY
            br.Route_Number
        ORDER BY
            br.Route_Number;
    '''

    return execute_query(connection, query)



# List all Neighbourhoods with the total number of Substances used, ordered by the total number of substances in descending order
def total_substance_neighbourhood(connection):
    query = '''
        SELECT
            n.Neighbourhood_Name,
            COUNT(s.Substance_Use_ID) AS Substance_Count
        FROM
            Neighbourhood n
            LEFT JOIN Substances s ON n.Neighbourhood_Name = s.Neighbourhood_Name
        GROUP BY
            n.Neighbourhood_Name
        ORDER BY
            Substance_Count DESC;
    '''

    return execute_query(connection, query)



# Retrieve the total count of Lane Closures for each Street and Street Type, ordered by Street Name and Street Type
def count_lane_closure_street(connection):
    query = '''
        SELECT
            lc.Street_Name,
            lc.Street_Type,
            COUNT(lc.Lane_Closure_ID) AS Closure_Count
        FROM
            Lane_Closure lc
            LEFT JOIN Street s ON lc.Street_Name = s.Street_Name AND lc.Street_Type = s.Street_Type
        GROUP BY
            lc.Street_Name, lc.Street_Type
        ORDER BY
            lc.Street_Name, lc.Street_Type;
    '''

    return execute_query(connection, query)



# List all Streets and their respective Paystation information, ordered by Street Name
def street_paystation(connection):
    query = '''
        SELECT
            s.Street_Name,
            s.Street_Type,
            p.Paystation_ID,
            p.Time_Limit,
            p.Space
        FROM
            Street s
            LEFT JOIN Paystation p ON s.Street_Name = p.Street_Name AND s.Street_Type = p.Street_Type
        ORDER BY
            s.Street_Name, s.Street_Type;
    '''

    return execute_query(connection, query)


# No Neighbourhood_Name in Neighbourhood
# Retrieve the total count of Tow incidents for each Neighbourhood, ordered by Neighbourhood name
def count_tow_neighbourhood(connection):
    query = '''
        SELECT
            n.Neighbourhood_Name,
            COUNT(t.Tow_ID) AS Tow_Count
        FROM
            Neighbourhood n
            LEFT JOIN Tow t ON n.Neighbourhood_Name = t.Neighbourhood_Name
        GROUP BY
            n.Neighbourhood_Name
        ORDER BY
            n.Neighbourhood_Name;
    '''

    return execute_query(connection, query)



# List all Bus Stops with their corresponding Neighbourhood and Bus Route information, ordered by Bus Stop Number
def bus_stop_neighbourhood_bus_route(connection):
    query = '''
        SELECT
            bs.Bus_Stop_Number,
            bs.Longitude,
            bs.Latitude,
            n.Neighbourhood_Name,
            br.Route_Number,
            br.Route_Destination
        FROM
            Bus_Stop bs
            LEFT JOIN GPS_Point gp ON bs.Longitude = gp.Longitude AND bs.Latitude = gp.Latitude
            LEFT JOIN Neighbourhood n ON gp.Neighbourhood_Name = n.Neighbourhood_Name
            LEFT JOIN Bus_Route br ON bs.Route_Number = br.Route_Number AND bs.Route_Destination = br.Route_Destination
        ORDER BY
            bs.Bus_Stop_Number;
    '''

    return execute_query(connection, query)



# Retrieve the latest WFPS call for each Neighbourhood, ordered by Neighbourhood name
def latest_wfps_neighbourhood(connection):
    query = '''
        SELECT
            n.Neighbourhood_Name,
            w.Date,
            w.Reason,
            w.Call_Time
        FROM
            Neighbourhood n
            LEFT JOIN WFPS_Call w ON n.Neighbourhood_Name = w.Neighbourhood_Name
        ORDER BY
            n.Neighbourhood_Name;
    '''

    return execute_query(connection, query)


# No results because matching on GPS_Point
# List all Streets with the count of Bus Stops on each street, ordered by Street Name
def count_bus_stop_street(connection):
    query = '''
        SELECT
            s.Street_Name,
            s.Street_Type,
            COUNT(bs.Row_ID) AS Bus_Stop_Count
        FROM
            Street s
            LEFT JOIN GPS_Point gp ON s.Street_Name = gp.Street_Name AND s.Street_Type = gp.Street_Type
            LEFT JOIN Bus_Stop bs ON gp.Longitude = bs.Longitude AND gp.Latitude = bs.Latitude
        GROUP BY
            s.Street_Name, s.Street_Type
        ORDER BY
            s.Street_Name;
    '''

    return execute_query(connection, query)


# Find all Bus Stops within a given range in meters of all known GPS Points of a given Street Name and Type
def bus_stops_on_street(connection, street_name, street_type, meters):
    latitude_diff = mu.meters_to_latitude_difference(meters)
    longitude_diff = mu.meters_to_longitude_difference(meters)

    query = '''
        SELECT bus_stop.row_ID, bus_stop.longitude, bus_stop.latitude
        FROM bus_stop
        JOIN gps_point ON bus_stop.latitude = gps_point.latitude AND bus_stop.longitude = gps_point.longitude
        WHERE gps_point.street_name = %s AND gps_point.street_type = %s
        AND gps_point.latitude BETWEEN (bus_stop.latitude - %s) AND (bus_stop.latitude + %s)
        AND gps_point.longitude BETWEEN (bus_stop.longitude - %s) AND (bus_stop.longitude + %s);
    '''
    
    return execute_query(connection, query, (street_name, street_type, latitude_diff, latitude_diff, longitude_diff, longitude_diff))


# Find all Lane Closures in a given Neighbourhood
def lane_closures_in_neighbourhood(connection, neighbourhood):
    query = '''
        select lane_closure.lane_closure_id, lane_closure.date_from, lane_closure.date_to, lane_closure.latitude, lane_closure.longitude
        from neighbourhood
        join neighbourhood_street on neighbourhood.neighbourhood_name = neighbourhood_street.neighbourhood_name
        join lane_closure on lane_closure.street_name = neighbourhood_street.street_name and lane_closure.street_type = neighbourhood_street.street_type
        where neighbourhood.neighbourhood_name = %s;
    '''

    return execute_query(connection, query, (neighbourhood))

