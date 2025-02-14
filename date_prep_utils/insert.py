import pandas as pd
import random


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
df = df.sample(100000)
df['WFPS_Call_ID'] = [i for i in range(len(df))]

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

#-----------------------------------------Paystation----------------------------------------------------
csv_file_path = 'Paystation.csv'

table_name = 'Paystation'

df = pd.read_csv(csv_file_path)

print(df)

# Open a file to write the SQL statements
with open('Paystation.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float):
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

csv_file_path = 'Paystation.csv'

table_name = 'Paystation'

street = pd.read_csv('Street.csv')
stret = street['Street_Name'].unique()
type = street['Street_Type'].unique()
tup = street[['Street_Name', 'Street_Type']].drop_duplicates()
tup = list(tup.itertuples(index=False, name=None))
print(stret)
print(type)

df = pd.read_csv(csv_file_path)
print(df)

# Go over all rows, and split Date and Time
for index, row in df.iterrows():
    str2 = row['Street_Name']
    str1 = row['Street_Type']

    if (str2,str1) not in tup: 
        df.at[index, 'Street_Name'] = None


df = df.drop_duplicates()
print(df)

# Open a file to write the SQL statements
with open('Paystation.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float) or value == 'null':
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
#--------------------------------------------------------------------------------------------------------

#-----------------------------------GPS_Point----------------------------------------
csv_file_path = 'GPS_Point.csv'

table_name = 'GPS_Point'

# # Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Open a file to write the SQL statements
with open('GPS_Point_1.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float):
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

csv_file_path = 'Parking_Citation_Street.csv'

table_name = 'GPS_Point'

street = pd.read_csv('Street.csv')
stret = street['Street_Name'].unique()
type = street['Street_Type'].unique()
tup = street[['Street_Name', 'Street_Type']].drop_duplicates()
tup = list(tup.itertuples(index=False, name=None))

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df = df.drop_duplicates()

df = df[['Latitude', 'Longitude', 'Neighbourhood_Name', 'Street_Name', 'Street_Type']]
df = df.drop_duplicates(['Latitude', 'Longitude'])

# Go over all rows, and split Date and Time
for index, row in df.iterrows():
    str2 = row['Street_Name']
    str1 = row['Street_Type']

    if (str2,str1) not in tup: 
        df.at[index, 'Street_Name'] = "null"

df = df[df['Street_Name'] != "null"]
df = df[df['Latitude'] != 0]
df = df[df['Longitude'] != 0]
print(df)

# Open a file to write the SQL statements
with open('GPS_Point_3.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float):
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

csv_file_path = 'LaneClosure.csv'

table_name = 'GPS_Point'

street = pd.read_csv('Street.csv')
stret = street['Street_Name'].unique()
type = street['Street_Type'].unique()
tup = street[['Street_Name', 'Street_Type']].drop_duplicates()
tup = list(tup.itertuples(index=False, name=None))
print(stret)
print(type)

Ngh = pd.read_csv('Neighbourhood.csv')
Ngh = Ngh['Neighbourhood_Name'].unique()
print(Ngh)

# # Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

df = df[df['Street_Name'].isin(stret)]
df = df[df['Street_Type'].isin(type)]

# df['Citation_ID'] = [i for i in range(len(df))]
df['Neighbourhood_Name'] = [random.choice(Ngh) for _ in range(len(df))]

# Go over all rows, and split Date and Time
for index, row in df.iterrows():
    str2 = row['Street_Name']
    str1 = row['Street_Type']

    if (str2,str1) not in tup: 
        df.at[index, 'Street_Name'] = None

df = df[['Latitude', 'Longitude', 'Neighbourhood_Name', 'Street_Name', 'Street_Type']]

df = df.drop_duplicates(['Latitude', 'Longitude'])

df = df.dropna(subset=["Street_Name"])
df = df[df['Street_Type'] != None]
print(df)

# Open a file to write the SQL statements
with open('GPS_Point_5.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float):
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

csv_file_path = 'Parking_Cit_100k.csv'

table_name = 'GPS_Point'

street = pd.read_csv('Street.csv')
stret = street['Street_Name'].unique()
type = street['Street_Type'].unique()
tup = street[['Street_Name', 'Street_Type']].drop_duplicates()
tup = list(tup.itertuples(index=False, name=None))

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df = df.drop_duplicates()

df = df[['Latitude', 'Longitude', 'Neighbourhood_Name', 'Street_Name', 'Street_Type']]
df = df.drop_duplicates(['Latitude', 'Longitude'])

# Go over all rows, and split Date and Time
for index, row in df.iterrows():
    str2 = row['Street_Name']
    str1 = row['Street_Type']

    if (str2,str1) not in tup: 
        df.at[index, 'Street_Name'] = "null"

df = df[df['Street_Name'] != "null"]
df = df[df['Latitude'] != 0]
df = df[df['Longitude'] != 0]
print(df)


tup = df[['Latitude', 'Longitude']].drop_duplicates()
tup = list(tup.itertuples(index=False, name=None))
print(len(tup))


csv_file_path = 'Tow.csv'

table_name = 'GPS_Point'

street = pd.read_csv('Street.csv')
stret = street['Street_Name'].unique()
type = street['Street_Type'].unique()
tupp = street[['Street_Name', 'Street_Type']].drop_duplicates()
tupp = list(tupp.itertuples(index=False, name=None))


# # Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

df['Tow_ID'] = [i for i in range(len(df))]
df['Neighbourhood_Name'] = ["null" for _ in range(len(df))]

df = df.drop_duplicates(['Latitude', 'Longitude'])

# Go over all rows, and split Date and Time
for index, row in df.iterrows():
    str2 = row['Street_Name']
    str1 = row['Street_Type']
    lat = row['Latitude']
    long = row['Longitude']

    if (str2,str1) not in tupp: 
        df.at[index, 'Street_Name'] = None
    
    if (lat, long) in tup:
        df.at[index, 'Latitude'] = None

df = df[[ 'Latitude', 'Longitude', 'Neighbourhood_Name','Street_Name', 'Street_Type']]

df = df.dropna(subset=["Street_Name"])
df = df.dropna(subset=["Latitude"])
df = df.dropna(subset=["Longitude"])
df = df[df['Street_Type'] != None]
df = df[df['Latitude'] != None]
df = df[df['Longitude'] != None]
print(df)

# Open a file to write the SQL statements
with open('GPS_Point_Tow.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float) or value == "null":
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

csv_file_path = 'BusData.csv'

table_name = 'GPS_Point'


# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df = df.drop_duplicates()

df['Neighbourhood_Name'] = ['null' for _ in range(len(df))]
df['Street_Name'] = ['null' for _ in range(len(df))]
df['Street_Type'] = ['null' for _ in range(len(df))]

df = df[[ 'Latitude', 'Longitude', 'Neighbourhood_Name','Street_Name', 'Street_Type']]

df = df.drop_duplicates(['Latitude', 'Longitude'])

# Open a file to write the SQL statements
with open('GPS_Point_7.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float) or value == "null":
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


#-----------------------------------------Parking Violation----------------------------------------------------
csv_file_path = 'Parking_Violation.csv'

table_name = 'Parking_Violation'

# # Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Open a file to write the SQL statements
with open('Parking_Violation.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float):
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
#--------------------------------------------------------------------------------------------------------

#-----------------------------------------Parking Citation----------------------------------------------------
csv_file_path = 'Parking_Citation_Street.csv'

table_name = 'Parking_Citation'

street = pd.read_csv('Street.csv')
stret = street['Street_Name'].unique()
type = street['Street_Type'].unique()
tup = street[['Street_Name', 'Street_Type']].drop_duplicates()
tup = list(tup.itertuples(index=False, name=None))

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df = df.drop_duplicates()

df['Citation_ID'] = [i for i in range(len(df))]

df = df[['Citation_ID', 'Issue_Date', 'Time', 'Violation_Type', 'Longitude', 'Latitude', 'Street_Name', 'Street_Type']]
df = df.drop_duplicates()
print(df)

# Go over all rows, and split Date and Time
for index, row in df.iterrows():
    str2 = row['Street_Name']
    str1 = row['Street_Type']

    if (str2,str1) not in tup: 
        df.at[index, 'Street_Name'] = "null"

df = df[df['Street_Name'] != "null"]
df = df[df['Latitude'] != 0]
df = df[df['Longitude'] != 0]
df = df[['Citation_ID', 'Issue_Date', 'Time', 'Violation_Type', 'Longitude', 'Latitude']]
print(df)

# Open a file to write the SQL statements
with open('Parking_Citation_1.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float):
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


ParkVio = pd.read_csv('Parking_Violation.csv')
VioType = ParkVio['Violation_Type'].unique()
print(VioType)



csv_file_path = 'Parking_Cit_100k.csv'

table_name = 'Parking_Citation'

street = pd.read_csv('Street.csv')
stret = street['Street_Name'].unique()
type = street['Street_Type'].unique()
tup = street[['Street_Name', 'Street_Type']].drop_duplicates()
tup = list(tup.itertuples(index=False, name=None))

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df = df.drop_duplicates()
df['Citation_ID'] = [i for i in range(len(df))]
print(df)

# df = df.drop_duplicates(['Latitude', 'Longitude'])
df = df.drop_duplicates()

for index, row in df.iterrows():
    str2 = row['Street_Name']
    str1 = row['Street_Type']
    vt = row['Violation_Type']

    if (str2,str1) not in tup: 
        df.at[index, 'Street_Name'] = "null"
    
    if vt not in VioType:
        df.at[index, 'Violation_Type'] = "null"

df = df[df['Street_Name'] != "null"]
df = df[df['Latitude'] != 0]
df = df[df['Violation_Type'] != "null"]
df = df[df['Longitude'] != 0]
df = df[['Citation_ID', 'Issue_Date', 'Time', 'Violation_Type', 'Longitude', 'Latitude']]
print(df)

# Open a file to write the SQL statements
with open('Parking_Citation.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float):
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
#--------------------------------------------------------------------------------------------------------

#-----------------------------------------Lane Closure----------------------------------------------------
csv_file_path = 'LaneClosure.csv'

table_name = 'Lane_Closure'

street = pd.read_csv('Street.csv')
stret = street['Street_Name'].unique()
type = street['Street_Type'].unique()
tup = street[['Street_Name', 'Street_Type']].drop_duplicates()
tup = list(tup.itertuples(index=False, name=None))
print(stret)
print(type)

Ngh = pd.read_csv('Neighbourhood.csv')
Ngh = Ngh['Neighbourhood_Name'].unique()
print(Ngh)

# # Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

df = df[df['Street_Name'].isin(stret)]
df = df[df['Street_Type'].isin(type)]

df['Lane_Closure_ID'] = [i for i in range(len(df))]

# Go over all rows, and split Date and Time
for index, row in df.iterrows():
    str2 = row['Street_Name']
    str1 = row['Street_Type']

    if (str2,str1) not in tup: 
        df.at[index, 'Street_Name'] = None

df = df[['Lane_Closure_ID', 'Date_To', 'Date_From', 'Street_Name', 'Street_Type', 'Longitude', 'Latitude']]


df = df.drop_duplicates(['Latitude', 'Longitude'])

df = df.dropna(subset=["Street_Name"])
df = df[df['Street_Type'] != None]
print(df)

# Open a file to write the SQL statements
with open('Lane_Closure.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float):
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
# --------------------------------------------------------------------------------------------------------

#-------------------------------------------------Tow------------------------------------------------------
csv_file_path = 'Parking_Cit_100k.csv'

table_name = 'GPS_Point'

street = pd.read_csv('Street.csv')
stret = street['Street_Name'].unique()
type = street['Street_Type'].unique()
tup = street[['Street_Name', 'Street_Type']].drop_duplicates()
tup = list(tup.itertuples(index=False, name=None))

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df = df.drop_duplicates()

df = df[['Latitude', 'Longitude', 'Neighbourhood_Name', 'Street_Name', 'Street_Type']]
df = df.drop_duplicates(['Latitude', 'Longitude'])

# Go over all rows, and split Date and Time
for index, row in df.iterrows():
    str2 = row['Street_Name']
    str1 = row['Street_Type']

    if (str2,str1) not in tup: 
        df.at[index, 'Street_Name'] = "null"

df = df[df['Street_Name'] != "null"]
df = df[df['Latitude'] != 0]
df = df[df['Longitude'] != 0]
print(df)


tup = df[['Latitude', 'Longitude']].drop_duplicates()
tup = list(tup.itertuples(index=False, name=None))
print(len(tup))


csv_file_path = 'Tow.csv'

table_name = 'GPS_Point'

street = pd.read_csv('Street.csv')
stret = street['Street_Name'].unique()
type = street['Street_Type'].unique()
tupp = street[['Street_Name', 'Street_Type']].drop_duplicates()
tupp = list(tupp.itertuples(index=False, name=None))


# # Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

df['Tow_ID'] = [i for i in range(len(df))]
df['Neighbourhood_Name'] = ["null" for _ in range(len(df))]

df = df.drop_duplicates(['Latitude', 'Longitude'])

# Go over all rows, and split Date and Time
for index, row in df.iterrows():
    str2 = row['Street_Name']
    str1 = row['Street_Type']
    lat = row['Latitude']
    long = row['Longitude']

    if (str2,str1) not in tupp: 
        df.at[index, 'Street_Name'] = None
    
    if (lat, long) in tup:
        df.at[index, 'Latitude'] = None

df = df[[ 'Latitude', 'Longitude', 'Neighbourhood_Name','Street_Name', 'Street_Type']]

df = df.dropna(subset=["Street_Name"])
df = df.dropna(subset=["Latitude"])
df = df.dropna(subset=["Longitude"])
df = df[df['Street_Type'] != None]
df = df[df['Latitude'] != None]
df = df[df['Longitude'] != None]
print(df)

tuppp = df[['Latitude', 'Longitude']].drop_duplicates()
tuppp = list(tuppp.itertuples(index=False, name=None))
print(tuppp)
print(len(tuppp))

csv_file_path = 'Tow.csv'

table_name = 'Tow'

# # Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)


df['Tow_ID'] = [i for i in range(len(df))]

# Go over all rows, and split Date and Time
for index, row in df.iterrows():
    str2 = row['Street_Name']
    str1 = row['Street_Type']
    lat = row['Latitude']
    long = row['Longitude']

    if (str2,str1) not in tupp: 
        df.at[index, 'Street_Name'] = None
    
    if (lat, long) not in tup and (lat, long) not in tuppp:
        df.at[index, 'Latitude'] = None

df = df[['Tow_ID', 'Date', 'Time', 'Status', 'Street_Name', 'Street_Type', 'Longitude', 'Latitude']]
df = df.dropna(subset=["Street_Name"])
df = df.dropna(subset=["Latitude"])
df = df.dropna(subset=["Longitude"])
df = df[df['Street_Type'] != None]
df = df[df['Latitude'] != None]
df = df[df['Longitude'] != None]
print(df)

# Open a file to write the SQL statements
with open('Tow.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float):
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
#----------------------------------------------------------------------------------------------------------

#---------------------------------------------Bus_Route------------------------------------------------------
csv_file_path = 'Bus_Route.csv'

table_name = 'Bus_Route'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df = df.drop_duplicates()

df = df.dropna(subset=["Route_Destination"])
df = df.dropna(subset=["Route_Name"])
df = df.dropna(subset=["Route_Number"])
# df = df[df['Street_Type'] != None]
print(df)

# Open a file to write the SQL statements
with open('Bus_Route.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float):
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
# --------------------------------------------------------------------------------------------------------

#---------------------------------------------Bus_Stop------------------------------------------------------
csv_file_path = 'BusData_100k.csv'

table_name = 'Bus_Stop'

# # Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df = df.drop_duplicates()

df = df[['Row_ID', 'Bus_Stop_Number', 'Scheduled_Time', 'Date', 'Deviation', 'Route_Number', 'Route_Destination', 'Longitude', 'Latitude']]
df['Row_ID'] = [i for i in range(len(df))]

print(df)

# Open a file to write the SQL statements
with open('Bus_Stop.sql', 'w') as sql_file:
    for index, row in df.iterrows():
        # Prepare the values for the SQL statement
        values = []
        for value in row.values:
            if isinstance(value, int) or isinstance(value, float):
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
# --------------------------------------------------------------------------------------------------------