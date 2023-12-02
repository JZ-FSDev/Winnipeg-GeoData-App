import pandas as pd


#-----------------------------------Neighbourhood----------------------------------------
csv_file_path = 'Neighbourhood.csv'

table_name = 'Neighbourhood'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Open a file to write the SQL statements
with open('Neighbourhood.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int):
                # Add integer as is
                values.append(str(value))
            else:
                # Escape single quotes in strings and add quotes around the string
                escaped_value = str(value).replace("'", "''")
                values.append(f"'{escaped_value}'")

        values_str = ', '.join(values)
        columns = ', '.join(row.index)
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        
        # Write the SQL statement to the file
        sql_file.write(sql)
#--------------------------------------------------------------------------------------

#--------------------------------------Street-----------------------------------------

csv_file_path = 'Street.csv'

table_name = 'Street'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Open a file to write the SQL statements
with open('Street.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int):
                # Add integer as is
                values.append(str(value))
            else:
                # Escape single quotes in strings and add quotes around the string
                escaped_value = str(value).replace("'", "''")
                values.append(f"'{escaped_value}'")

        values_str = ', '.join(values)
        columns = ', '.join(row.index)
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        
        # Write the SQL statement to the file
        sql_file.write(sql)
#--------------------------------------------------------------------------------------

#--------------------------------------Neighbourhood_Street-----------------------------------------

csv_file_path = 'NeighBourhood_Street.csv'


table_name = 'NeighBourhood_Street'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Open a file to write the SQL statements
with open('Neighbourhood_street.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int):
                # Add integer as is
                values.append(str(value))
            else:
                # Escape single quotes in strings and add quotes around the string
                escaped_value = str(value).replace("'", "''")
                values.append(f"'{escaped_value}'")

        values_str = ', '.join(values)
        columns = ', '.join(row.index)
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        
        # Write the SQL statement to the file
        sql_file.write(sql)
#------------------------------------------------------------------------------------------------------

#-----------------------------------WFPS_Call----------------------------------------

csv_file_path = 'WFPS_Call.csv'

table_name = 'WFPS_Call'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Open a file to write the SQL statements
with open('WFPS_Call.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int):
                # Add integer as is
                values.append(str(value))
            else:
                # Escape single quotes in strings and add quotes around the string
                escaped_value = str(value).replace("'", "''")
                values.append(f"'{escaped_value}'")

        values_str = ', '.join(values)
        columns = ', '.join(row.index)
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        
        # Write the SQL statement to the file
        sql_file.write(sql)
#------------------------------------------------------------------------------------------------------

#-----------------------------------`Substances`----------------------------------------

csv_file_path = 'Substances.csv'

table_name = 'Substances'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Open a file to write the SQL statements
with open('Substances.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int):
                # Add integer as is
                values.append(str(value))
            else:
                # Escape single quotes in strings and add quotes around the string
                escaped_value = str(value).replace("'", "''")
                values.append(f"'{escaped_value}'")

        values_str = ', '.join(values)
        columns = ', '.join(row.index)
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n"
        
        # Write the SQL statement to the file
        sql_file.write(sql)
#------------------------------------------------------------------------------------------------------