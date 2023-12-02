import pyodbc
import config_reader as cr


script_file = "script.sql"  # Script to generate our tables and insert our data


# Logs into the sql server and returns a new connection
def connect_to_sql_server():

    # Read database credentials from a configuration file
    username, password = cr.get_username_password()

    # Define the connection string
    server = 'uranium.cs.umanitoba.ca'
    database = 'cs3380'
    driver = '{SQL Server}'
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};'

    # Connect to the database
    try:
        connection = pyodbc.connect(connection_string)
        return connection
    except pyodbc.Error as e:
        print(f"Error connecting to the database: {e}")
        exit(1)


# Populates the database by executing the sql script on the MSSQL server
def populate_database(connection):

    # Read and execute the SQL script to populate the database
    try:
        cursor = connection.cursor()

        with open(script_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        print("Script executed successfully.")
    except FileNotFoundError:
        print(f"Could not find the script file: {script_file}")
    except pyodbc.Error as e:
        print(f"Error executing the script: {e}")


# Executes the given query on via the given connection and returns the result set
def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows

    except pyodbc.Error as e:
        print(f"Error executing the query: {e}")

    finally:
        # Close the cursor
        cursor.close() 


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

    execute_query(connection, query)


# List all Streets along with the count of Parking Citations for each street, ordered by the street name
def count_parking_citation_street(connection):
    query = '''
        SELECT
            s.Street_Name,
            COUNT(pc.Citation_ID) AS Citation_Count
        FROM
            Street s
            LEFT JOIN GPS_Point gp ON s.Street_Name = gp.Street_Name AND s.Street_Type = gp.Street_Type
            LEFT JOIN Parking_Citation pc ON gp.Longitude = pc.Longitude AND gp.Latitude = pc.Latitude
        GROUP BY
            s.Street_Name
        ORDER BY
            s.Street_Name;
    '''

    execute_query(connection, query)


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

    execute_query(connection, query)



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

    execute_query(connection, query)



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

    execute_query(connection, query)



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

    execute_query(connection, query)



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

    execute_query(connection, query)



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

    execute_query(connection, query)



# Retrieve the latest WFPS call for each Neighbourhood, ordered by Neighbourhood name
def latest_wfps_neighbourhood(connection):
    query = '''
        SELECT
            n.Neighbourhood_Name,
            w.Call_Date,
            w.Reason,
            w.Call_Time
        FROM
            Neighbourhood n
            LEFT JOIN WFPS_Call w ON n.Neighbourhood_Name = w.Neighbourhood_Name
        ORDER BY
            n.Neighbourhood_Name, w.Call_Date DESC;
    '''

    execute_query(connection, query)


# List all Streets with the count of Bus Stops on each street, ordered by Street Name
def count_bus_stop_street(connection):
    query = '''
        SELECT
            s.Street_Name,
            COUNT(bs.Row_ID) AS Bus_Stop_Count
        FROM
            Street s
            LEFT JOIN GPS_Point gp ON s.Street_Name = gp.Street_Name AND s.Street_Type = gp.Street_Type
            LEFT JOIN Bus_Stop bs ON gp.Longitude = bs.Longitude AND gp.Latitude = bs.Latitude
        GROUP BY
            s.Street_Name
        ORDER BY
            s.Street_Name;
    '''

    execute_query(connection, query)