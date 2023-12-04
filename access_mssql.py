import pymssql
import config_reader as cr


script_file = "script.sql"  # Script to generate our tables
street_file = "Street.sql"  # Script to insert Street info
neighbourhood_file = "Neighbourhood.sql"  # Script to insert Neighbourhood info
neighbourhood_street_file = "Neighbourhood_street.sql"  # Script to insert Neighbourhood_steet info
substance_file = "Substances.sql"  # Script to insert Substance info
wfps_call_file_1 = "WFPS_Call_1.sql"  # Script to insert WFPS Call part 1 info
wfps_call_file_2 = "WFPS_Call_2.sql"  # Script to insert WFPS Call part 2 info
gps_point_file_1 = "GPS_Point_1.sql"
gps_point_file_2 = "GPS_Point_2.sql"
gps_point_file_3 = "GPS_Point_3.sql"
gps_point_file_4 = "GPS_Point_4.sql"
gps_point_file_5 = "GPS_Point_5.sql"
gps_point_file_6 = "GPS_Point_6.sql"
gps_point_file_7 = "GPS_Point_7.sql"
paystation_file = "Paystation.sql"
parking_violation_file = "Parking_Violation.sql"
parking_citation_file_1 = "Parking_Citation_1.sql"
parking_citation_file_2 = "Parking_Citation_2.sql"
lane_closure_file = "Lane_Closure.sql"
tow_file = "Tow.sql"
bus_route_file = "Bus_Route.sql"
bus_stop_file_1 = "Bus_Stop_1.sql"
bus_stop_file_2 = "Bus_Stop_2.sql"
bus_stop_file_3 = "Bus_Stop_3.sql"


### Consider using multi threaded insert and transactions for the insert ###


# Logs into the sql server and returns a new connection
import pymssql

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

        # with open(wfps_call_file_1) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("WFPS_Calls part 1 inserted successfully.")

        # with open(wfps_call_file_2) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("WFPS_Calls part 2 inserted successfully.")

        # with open(gps_point_file_1) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point part 1 inserted successfully.")

        # with open(gps_point_file_2) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point part 2 inserted successfully.")

        # with open(gps_point_file_3) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point part 3 inserted successfully.")

        # with open(gps_point_file_4) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point part 4 inserted successfully.")

        # with open(gps_point_file_5) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point part 5 inserted successfully.")

        # FK
        # with open(gps_point_file_6) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point part 6 inserted successfully.")     

        # with open(gps_point_file_7) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("GPS_Point part 7 inserted successfully.")             

        # # Time Limit is String
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

        # FK
        with open(parking_citation_file_1) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Parking_Citations part 1 inserted successfully.")       

        # FK
        with open(parking_citation_file_2) as script:
            script_content = script.read()
            cursor.execute(script_content)
        connection.commit()
        print("Parking_Citations part 2 inserted successfully.")                       

        # with open(lane_closure_file) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Lane_Closures inserted successfully.")        

        # FK ERROR
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

        # with open(bus_stop_file_1) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Bus_Stops part 1 inserted successfully.")  
                     
        # with open(bus_stop_file_2) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Bus_Stops part 2 inserted successfully.")  

        # with open(bus_stop_file_3) as script:
        #     script_content = script.read()
        #     cursor.execute(script_content)
        # connection.commit()
        # print("Bus_Stops part 3 inserted successfully.")  

        print("All data inserted successfully")
    except FileNotFoundError:
        print(f"Could not find the script file: {script_file}")
    except pymssql.Error as e:
        print(f"Error executing the script: {e}")


# Executes the given query on via the given connection and returns the result set
def execute_query(connection, query):
    try:
        cursor = connection.cursor()
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


