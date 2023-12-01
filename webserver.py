import pandas as pd
import plotly.express as px
import numpy as np
import plotly.offline as offline
import pyodbc



config_file = "auth.cfg"  # Config file containing the MSSQL server username and password
script_file = 'script.sql'  # Script to generate our tables and insert our data

# Logs into the sql server and returns a new connection and cursor
def login_to_sql_server():
    # Read database credentials from a configuration file

    credentials = {}

    try:
        with open(config_file) as f:
            for line in f:
                key, value = map(str.strip, line.split('=', 1))
                credentials[key] = value
    except FileNotFoundError:
        print("Could not find config file.")
        exit(1)
    except ValueError:
        print("Invalid config file format.")
        exit(1)

    # Extract username and password
    username = credentials.get('username')
    password = credentials.get('password')

    if username is None or password is None:
        print("Username or password not provided.")
        exit(1)

    # Define the connection string
    server = 'uranium.cs.umanitoba.ca'
    database = 'cs3380'
    driver = '{SQL Server}'
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};'

    # Connect to the database
    try:
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        return connection, cursor
    except pyodbc.Error as e:
        print(f"Error connecting to the database: {e}")
        exit(1)

# Populates the database by executing the sql script on the MSSQL server
def populate_database(cursor):

    # Read and execute the SQL script to populate the database
    try:
        with open(script_file) as script:
            script_content = script.read()
            cursor.execute(script_content)
        print("Script executed successfully.")
    except FileNotFoundError:
        print(f"Could not find the script file: {script_file}")
    except pyodbc.Error as e:
        print(f"Error executing the script: {e}")


# Boiler code as template for when we write our own queries
def test_query(connection, cursor):
    # Execute the SQL query
    select_query = '''
        SELECT firstname, lastname, provinces.name
        FROM people
        JOIN provinces ON people.provinceID = provinces.provinceID
    '''

    try:
        cursor.execute(select_query)
        rows = cursor.fetchall()

        # Print results from select statement
        for row in rows:
            print(f"{row.firstname} {row.lastname} lives in {row.name}")

    except pyodbc.Error as e:
        print(f"Error executing the query: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


# Updates the interactive map displayed on the website
def update_map():
    # Set fixed coordinates for Winnipeg
    winnipeg_latitude = 49.8951
    winnipeg_longitude = -97.1384

    # Creating a DataFrame with fixed coordinates for Winnipeg and random animal names
    data = {
        'Latitude': np.random.uniform(low=winnipeg_latitude - 0.1, high=winnipeg_latitude + 0.1, size=10),
        'Longitude': np.random.uniform(low=winnipeg_longitude - 0.1, high=winnipeg_longitude + 0.1, size=10),
        'Animal': np.random.choice(['Lion', 'Elephant', 'Giraffe', 'Zebra', 'Kangaroo'], size=10)
    }

    df = pd.DataFrame(data)

    # Create a scatter plot with a constant size
    fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', text='Animal',
                            center=dict(lat=df.Latitude.mean(), lon=df.Longitude.mean()),
                            zoom=10, mapbox_style='open-street-map', height=550,
                            size_max=15)  # Set the maximum size of the dots

    # Save the interactive map as an HTML file
    offline.plot(fig, filename='interactive_map.html', auto_open=False)


def main():
    conncection, cursor = login_to_sql_server()
    populate_database(cursor)



if __name__ == "__main__":
    main()