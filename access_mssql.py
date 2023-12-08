import pymssql
import config_reader as cr
import math_utils as mu


script_relative_path = "sql_files/"

# Define SQL script file paths
drop_create_table_file = script_relative_path + "Drop_Create_Tables.sql" 
street_file = script_relative_path + "Street.sql" 
neighbourhood_file = script_relative_path + "Neighbourhood.sql"  
neighbourhood_street_file = script_relative_path + "Neighbourhood_Street.sql"  
substance_use_file = script_relative_path + "Substance_Use.sql"  
wfps_call_file = script_relative_path + "WFPS_Call.sql" 
gps_point_file_address = script_relative_path + "GPS_Point_Addresses.sql"
gps_point_file_bus_stop = script_relative_path + "GPS_Point_Bus_Stop.sql"
gps_point_file_lane_closure = script_relative_path + "GPS_Point_Lane_Closure.sql"
gps_point_park_citation = script_relative_path + "GPS_Point_Park_Citation.sql"
gps_point_file_paystation = script_relative_path + "GPS_Point_Paystation.sql"
gps_point_tow = script_relative_path + "GPS_Point_Tow.sql"
parking_violation_file = script_relative_path + "Parking_Violation.sql"
paystation_file = script_relative_path + "Paystation.sql"
parking_citation_file = script_relative_path + "Parking_Citation.sql"
lane_closure_file = script_relative_path + "Lane_Closure.sql"
tow_file = script_relative_path + "Tow.sql"
bus_route_file = script_relative_path + "Bus_Route.sql"
bus_stop_file = script_relative_path + "Bus_Stop.sql"
indexes_file = script_relative_path + "Indexes.sql"

ADJACENT_RADIUS = 100  # 100 meter range for considering two entities to be adjacent to each other
RECENT_IMPACT_TIME = 15  # Within 15 minutes for considering two events impact one another 

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

        with open(drop_create_table_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Drop and Create Tables executed successfully.")

        with open(street_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Streets inserted successfully.")

        with open(neighbourhood_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Neighbourhoods inserted successfully.")

        with open(neighbourhood_street_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Neighbourhood_Streets inserted successfully.")

        with open(substance_use_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Substance Uses inserted successfully.")

        with open(wfps_call_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("WFPS_Calls inserted successfully.")

        with open(gps_point_file_address) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("GPS_Point addresses inserted successfully.")

        with open(gps_point_file_bus_stop) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("GPS_Point bus stops inserted successfully.")

        with open(gps_point_park_citation) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("GPS_Point parking citations inserted successfully.")

        with open(gps_point_file_paystation) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("GPS_Point paystations inserted successfully.")

        with open(gps_point_file_lane_closure) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("GPS_Point lane closures inserted successfully.")

        with open(gps_point_tow) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("GPS_Point tows inserted successfully.")        

        with open(paystation_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Paystations inserted successfully.")

        with open(parking_violation_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Parking_Violations inserted successfully.")

        with open(parking_citation_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Parking_Citations inserted successfully.")                            

        with open(lane_closure_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Lane_Closures inserted successfully.")        

        with open(tow_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Tows inserted successfully.")  

        with open(bus_route_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Bus_Routes inserted successfully.")  

        with open(bus_stop_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Bus_Stops inserted successfully.")  

        with open(indexes_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Indexes created successfully.")  

        print("All data inserted successfully")
    except FileNotFoundError:
        print(f"Could not find the script file")
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



# Retrieve Neighbourhood names along with the total number of houses and the count of WFPS calls for each Neighbourhood
def count_wfps_call_neighbourhood(connection):
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
            Call_Count;
    '''

    return execute_query(connection, query)


# Retrieve the total count of Parking Citations and the sum of all violation fine amounts for each Street
def count_parking_citation_street(connection):
    query = '''
        SELECT
            s.Street_Name,
            s.Street_Type,
            COUNT(pc.Citation_ID) AS Citation_Count,
            sum(pv.fine_amount) as Total_Fines
        FROM
            Street s
            LEFT JOIN GPS_Point gp ON s.Street_Name = gp.Street_Name AND s.Street_Type = gp.Street_Type
            LEFT JOIN Parking_Citation pc ON gp.Longitude = pc.Longitude AND gp.Latitude = pc.Latitude
            left join parking_violation pv on pc.violation_type = pc.violation_type
        GROUP BY
            s.Street_Name, s.Street_Type
        ORDER BY
            Citation_Count;
    '''

    return execute_query(connection, query)


# Retrieve the Bus Routes along with the average deviation of each stop for each route
def bus_route_avg_deviation(connection):
    query = '''
        WITH dev_sum AS (
            SELECT
                br.Route_Number,
                br.Route_Destination,
                SUM(bs.Deviation) AS Deviation
            FROM
                Bus_Route br
                JOIN Bus_Stop bs ON br.Route_Number = bs.Route_Number AND br.Route_Destination = bs.Route_Destination
            GROUP BY
                br.Route_Number, br.Route_Destination
        ),
        dev_count AS (
            SELECT
                br.Route_Number,
                br.Route_Destination,
                COUNT(*) AS Count
            FROM
                Bus_Route br
                JOIN Bus_Stop bs ON br.Route_Number = bs.Route_Number AND br.Route_Destination = bs.Route_Destination
            GROUP BY
                br.Route_Number, br.Route_Destination
        )
        SELECT
            dev_sum.Route_Number,
            dev_sum.Route_Destination,
            dev_sum.Deviation / dev_count.Count AS Average_Deviation
        FROM
            dev_sum
            JOIN dev_count ON dev_sum.Route_Number = dev_count.Route_Number AND dev_sum.Route_Destination = dev_count.Route_Destination
        ORDER BY
            dev_sum.Route_Number, dev_count.Route_Number;
    '''

    return execute_query(connection, query)




# Retrieve Neighbourhood names along with the total number of houses and the count of Substance Uses for each Neighbourhood
def count_substance_neighbourhood(connection):
    query = '''
        SELECT
            n.Neighbourhood_Name,
            n.Number_OF_Houses,
            COUNT(s.Substance_Use_ID) AS Substance_Count
        FROM
            Neighbourhood n
            LEFT JOIN Substance_use s ON n.Neighbourhood_Name = s.Neighbourhood_Name
        GROUP BY
            n.Neighbourhood_Name
        ORDER BY
            Substance_Count DESC;
    '''

    return execute_query(connection, query)



# Retrieve the total count of Lane Closures for each Street
def count_lane_closure_street(connection):
    query = '''
        SELECT
            lc.Street_Name,
            lc.Street_Type,
            COUNT(lc.Lane_Closure_ID) AS Closure_Count
        FROM
            Lane_Closure lc
            JOIN Street s ON lc.Street_Name = s.Street_Name AND lc.Street_Type = s.Street_Type
        GROUP BY
            lc.Street_Name, lc.Street_Type
        ORDER BY
            Closure_Count;
    '''

    return execute_query(connection, query)



# List all Streets and their respective Paystation id, time_limit, and space, ordered by Street name and type. Displays the Paystations in the interactive map
def street_paystation(connection):
    query = '''
        SELECT
            s.Street_Name,
            s.Street_Type,
            p.Paystation_ID,
            p.Time_Limit,
            p.Space,
            p.latitude,
            p.longitude
        FROM
            Street s
            JOIN Paystation p ON s.Street_Name = p.Street_Name AND s.Street_Type = p.Street_Type
        ORDER BY
            s.Street_Name, s.Street_Type;
    '''

    return execute_query(connection, query)


# Find all Tows ids and their status in a given Neighbourhood. Displays the Tows in the interactive map
def tows_in_neighbourhood(connection, neighbourhood):
    query = '''
        SELECT
            tow.tow_id,
            tow.latitude,
            tow.longitude,
            tow.status
        FROM
            tow
            join neighbourhood_street on neighbourhood_street.street_name = tow.street_name and neighbourhood_street.street_type = tow.street_type
            where neighbourhood_street.neighbourhood_name = %s
        ORDER BY
            tow.tow_id;
    '''

    return execute_query(connection, query, (neighbourhood))


# Retrieves all Substance Use ids, dates, times, and substances for a given Neighbourhood
def substances_in_neighbourhood(connection, neighbourhood):
    query = '''
        SELECT
            su.substance_use_id,
            su.substance,
            su.date,
            su.time
        FROM
            Neighbourhood n
            JOIN substance_use su ON n.Neighbourhood_Name = su.Neighbourhood_Name
            where n.neighbourhood_name = %s
        ORDER BY
            su.time;
    '''

    return execute_query(connection, query, (neighbourhood))


# List all unique Bus Route numbers, destinations, and names between a given date and time range that run through a given neighbourhood
def bus_route_in_neighbourhood_between_date_time(connection, start_date, start_time, end_date, end_time, neighbourhood):
    latitude_diff = mu.meters_to_latitude_difference(int(ADJACENT_RADIUS))
    longitude_diff = mu.meters_to_longitude_difference(int(ADJACENT_RADIUS), latitude_diff)

    print(start_time, end_time, start_date, end_date, neighbourhood)

    query = '''
        SELECT DISTINCT
            bus_route.route_number,
            bus_route.route_destination,
            bus_route.route_name
        FROM
            bus_route
        JOIN
            bus_stop ON bus_route.route_number = bus_stop.route_number AND bus_route.route_destination = bus_stop.route_destination
        JOIN
            gps_point ON gps_point.latitude BETWEEN (bus_stop.latitude - %s) AND (bus_stop.latitude + %s)
            AND gps_point.longitude BETWEEN (bus_stop.longitude - %s) AND (bus_stop.longitude + %s)
        WHERE
            bus_stop.scheduled_time between %s and %s and bus_stop.date between %s and %s and %s = gps_point.neighbourhood_name;
    '''

    return execute_query(connection, query, (latitude_diff, latitude_diff, longitude_diff, longitude_diff, start_time, end_time, start_date, end_date, neighbourhood))


# Retrieve all the WFPS Call ids, dates, call times, and reasons for a given Neighbourhood
def wfps_in_neighbourhood(connection, neighbourhood):
    query = '''
        SELECT
            w.WFPS_Call_id,
            w.Date,
            w.Reason,
            w.Call_Time
        FROM
            Neighbourhood n
            JOIN WFPS_Call w ON n.Neighbourhood_Name = w.Neighbourhood_Name
            where n.neighbourhood_name = %s
        ORDER BY
            su.time;
    '''

    return execute_query(connection, query, (neighbourhood))


# List all Streets with the count of Bus Stops on each street
def count_bus_stop_street(connection):
    latitude_diff = mu.meters_to_latitude_difference(int(ADJACENT_RADIUS))
    longitude_diff = mu.meters_to_longitude_difference(int(ADJACENT_RADIUS), latitude_diff)

    query = '''
        SELECT
            gps.Street_Name,
            gps.Street_Type,
            COUNT(bs.Row_ID) AS Bus_Stop_Count
        FROM
            gps_point gps
        JOIN
            bus_stop bs ON
                bs.Latitude BETWEEN (gps.Latitude - %s) AND (gps.Latitude + %s)
                AND bs.Longitude BETWEEN (gps.Longitude - %s) AND (gps.Longitude + %s)
        WHERE
            gps.Street_Name IS NOT NULL AND gps.Street_Type IS NOT NULL
        GROUP BY
            gps.Street_Name, gps.Street_Type
        ORDER BY
            Bus_Stop_Count desc;
    '''

    return execute_query(connection, query, (latitude_diff, latitude_diff, longitude_diff, longitude_diff))


# Find all Bus Stop ids, scheduled times, dates, and route names within a given range in meters of all known GPS Points of a given Street name and type. Displays the Bus Stops on the interactive map
def bus_stops_on_street(connection, street_name, street_type, meters):
    latitude_diff = mu.meters_to_latitude_difference(int(meters))
    longitude_diff = mu.meters_to_longitude_difference(int(meters), latitude_diff)

    query = '''
        SELECT DISTINCT
            bus_stop.row_ID,
            bus_stop.longitude,
            bus_stop.latitude,
            bus_stop.date,
            bus_stop.scheduled_time,
            bus_route.route_name
        FROM
            bus_stop
        JOIN
            gps_point ON gps_point.latitude BETWEEN (bus_stop.latitude - %s) AND (bus_stop.latitude + %s)
                AND gps_point.longitude BETWEEN (bus_stop.longitude - %s) AND (bus_stop.longitude + %s)
        JOIN
            bus_route ON bus_route.route_number = bus_stop.route_number
                AND bus_route.route_destination = bus_stop.route_destination
        WHERE
            gps_point.street_name = %s
            AND gps_point.street_type = %s
        ORDER BY
            bus_stop.date;

    '''
    
    return execute_query(connection, query, (latitude_diff, latitude_diff, longitude_diff, longitude_diff, street_name, street_type))


# Find all Lane Closure ids and date ranges in a given Neighbourhood. Displays the center locations of the Lane Closures on the interactive map
def lane_closures_in_neighbourhood(connection, neighbourhood):
    query = '''
        SELECT
            lane_closure.lane_closure_id,
            lane_closure.date_from,
            lane_closure.date_to,
            lane_closure.latitude,
            lane_closure.longitude
        FROM
            neighbourhood
        JOIN
            neighbourhood_street ON neighbourhood.neighbourhood_name = neighbourhood_street.neighbourhood_name
        JOIN
            lane_closure ON lane_closure.street_name = neighbourhood_street.street_name
                        AND lane_closure.street_type = neighbourhood_street.street_type
        WHERE
            neighbourhood.neighbourhood_name = %s
        ORDER BY
            lane_closure.lane_closure_id;
    '''

    return execute_query(connection, query, (neighbourhood))


# Find all Parking Citations ids, fine amounts and types and Tow ids and statuses which occurred on the same location of a given Street name and type. Displays the shared locations of the Tows and Parking Citations on the interative map
def parking_citation_and_tow_on_street(connection, street_name, street_type):
    query = '''
        SELECT
            parking_citation.citation_id,
            parking_violation.fine_amount,
            parking_citation.violation_type,
            tow.tow_id,
            tow.status,
            tow.latitude,
            tow.longitude
        FROM
            parking_citation
        JOIN
            tow ON tow.latitude = parking_citation.latitude AND tow.longitude = parking_citation.longitude
        JOIN
            parking_violation ON parking_violation.violation_type = parking_citation.violation_type
        WHERE
            tow.street_name = %s
            AND tow.street_type = %s
        ORDER BY
            parking_violation.fine_amount DESC;
    '''

    return execute_query(connection, query, (street_name, street_type))


# Transit delays that might have been caused due to Tows happening nearby. Reports nearby Bus Stop id, deviation, route destination, route number, route name, and Tow ids. Displays the locations of the Tows and Bus Stops on the interative map
def transit_delay_due_to_tow(connection):
    latitude_diff = mu.meters_to_latitude_difference(ADJACENT_RADIUS)
    longitude_diff = mu.meters_to_longitude_difference(ADJACENT_RADIUS, latitude_diff)

    query = '''
        SELECT distinct
            bs.Latitude, bs.Longitude, bs.Scheduled_Time, 
            bs.Deviation,
            bs.Route_Destination, bs.Route_Number,
            Tow.Latitude, Tow.Longitude,
            br.Route_Name,
            tow.tow_id,
            bs.row_id
        FROM
            bus_stop bs
        JOIN
            Bus_Route br ON
                br.Route_Number = bs.Route_Number AND br.Route_Destination = br.Route_Destination
        JOIN
            Tow ON
                bs.Latitude BETWEEN (Tow.Latitude - %s) AND (Tow.Latitude + %s)
                AND bs.Longitude BETWEEN (Tow.Longitude - %s) AND (Tow.Longitude + %s)
        WHERE
            bs.Date = Tow.Date AND
            bs.Deviation < 0 AND 
            bs.Scheduled_Time BETWEEN DATEADD(MINUTE, %s, Tow.Time) AND DATEADD(MINUTE, %s, Tow.Time)
        ORDER BY
            bs.Deviation;
    '''
    return execute_query(connection, query, (latitude_diff, latitude_diff, longitude_diff, longitude_diff, -RECENT_IMPACT_TIME, RECENT_IMPACT_TIME))


# Transit delays that might have been caused due to Parking_Citations nearby. Reports nearby Bus Stop id, deviation, route destination, route number, route name, and Parking Citation ids. Displays the locations of the Parking Citations and Bus Stops on the interative map
def transit_delay_due_to_citation(connection):
    latitude_diff = mu.meters_to_latitude_difference(ADJACENT_RADIUS)
    longitude_diff = mu.meters_to_longitude_difference(ADJACENT_RADIUS, latitude_diff)

    query = '''
        SELECT distinct 
            bs.Latitude, bs.Longitude, bs.Scheduled_Time, 
            bs.Deviation,
            bs.Route_Destination, bs.Route_Number,
            pk.Latitude, pk.Longitude,
            br.Route_Name,
            pk.citation_id,
            bs.row_id
        FROM
            bus_stop bs
        JOIN
            Bus_Route br ON
            br.Route_Number = bs.Route_Number AND br.Route_Destination = br.Route_Destination
        JOIN
            Parking_Citation pk ON
                bs.Latitude BETWEEN (pk.Latitude - %s) AND (pk.Latitude + %s)
                AND bs.Longitude BETWEEN (pk.Longitude - %s) AND (pk.Longitude + %s)
        WHERE
            bs.Date = pk.Issue_Date AND
            bs.Deviation < 0 AND 
            bs.Scheduled_Time BETWEEN DATEADD(MINUTE, %s, bs.Scheduled_Time) AND DATEADD(MINUTE, %s, bs.Scheduled_Time)
        ORDER BY
            bs.Deviation;
    '''
    return execute_query(connection, query, (latitude_diff, latitude_diff, longitude_diff, longitude_diff, -RECENT_IMPACT_TIME, RECENT_IMPACT_TIME))