import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

#Data Clean up

#--------------------------Lane closure------------------------
data = pd.read_csv("Lane_Closure_20231019.csv")

#Drop the clumns not required
data = data[['Primary Street', 'Date Closed - From', 'Date Closed - To', 'Latitude', 'Longitude']]

#Insert a new column into dataframe
data.insert(1, 'Street_Type', '')

#Rename columns
data.rename(columns = {'Primary Street':'Street_Name', 'Date Closed - From':'Date_From', 'Date Closed - To':'Date_To'}, inplace = True)

#Go over all rows, and split street name and type
for index, row in data.iterrows():
    tokens = row['Street_Name'].split()

    if(len(tokens) == 1):
        data.at[index, 'Street_Name'] = tokens[0]
    else:
        # Reconstructing 'Street_Name' without the last token
        data.at[index, 'Street_Name'] = ' '.join(tokens[:-1])
        
        # Assigning the last token to 'Street_Type'
        data.at[index, 'Street_Type'] = tokens[-1]

# Convert to datetime
data['Date_From'] = pd.to_datetime(data['Date_From'], format='%B %d %Y').dt.date
data['Date_To'] = pd.to_datetime(data['Date_To'], format='%B %d %Y').dt.date

#Remove the direction
for index, row in data.iterrows():
    tokens = row['Street_Name'].split()
    temp = row['Street_Type']

    if(len(temp) == 1):
        data.at[index, 'Street_Name'] = tokens[0]
        data.at[index, 'Street_Type'] = tokens[1]

#Chnage street types to maintain consistency
dictionary = {'Av':'AVE', 'St':'ST', 'Rd':'RD', 'Ln':'LANE', 'Dr':'DR', 'Cr':'CRES', 'Bv':'BLVD', 
              'Hw':'HWY', 'Bridge':'Bridge', 'Rw':'ROW', 'Cv':'COVE',
              'Ct':'CRT', 'By':'BAY', 'Pl':'PL', 'Pk':'PK', 'Wy':'WAY', 'Gate':'GATE', 'Fwy':'FWY'}

for index, row in data.iterrows():
    type = row['Street_Type']
    data.at[index, 'Street_Type'] = dictionary[type]


for index, row in data.iterrows():
    str = row['Street_Name']

    str = str.upper()
    data.at[index, 'Street_Name'] = str

# Write DataFrame to a CSV file
data.to_csv('LaneClosure.csv', index=False)
#-------------------------------------------------------------------------

#--------------------------Parking Citation------------------------
data = pd.read_csv("Parking_Contravention__Citations.csv", dtype={6: object})

new_data = data[['Issue Date', 'Violation', 'Location']]

#Drop all rows with NaN value in latitide and longitude
data = new_data.dropna(subset=['Location'])

# Splitting the Location column and expanding into two columns
split = data['Location'].str.strip('()').str.split(', ', expand=True)

# Converting the new columns to float
data.loc[:,'Latitude'] = split[0].astype(float)
data.loc[:,'Longitude'] = split[1].astype(float)

#Drop the Location column from data frame
data = data[['Issue Date', 'Violation', 'Latitude', 'Longitude']]

#Insert new columns into dataframe
data.insert(1, 'Issue_Date', '')
data.insert(2, 'Time', '')

#Go over all rows, and split Date and Time
for index, row in data.iterrows():
    date_time_str = row['Issue Date']

    date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y %I:%M:%S %p')

    # Extract date and time
    data.at[index, 'Issue_Date'] = date_time_obj.date()
    data.at[index, 'Time'] = date_time_obj.time()


#Drop the Issue Date column from data frame
data = data[['Issue_Date', 'Time', 'Violation', 'Latitude', 'Longitude']]

#Rename columns
data.rename(columns = {'Violation':'Violation_Type'}, inplace = True)

#store it to csv
data.to_csv('Parking_Citation.csv', index=False)
#-------------------------------------------------------------------------

#------------------------------Citation_Street------------------------------
data = pd.read_csv("Parking_Contravention__Citations.csv", dtype={6: object})

new_data = data[['Issue Date', 'Violation', 'Location', 'Street']]

#Drop all rows with NaN value in latitide and longitude
data = new_data.dropna(subset=['Location'])

# Splitting the Location column and expanding into two columns
split = data['Location'].str.strip('()').str.split(', ', expand=True)

# Converting the new columns to float
data.loc[:,'Latitude'] = split[0].astype(float)
data.loc[:,'Longitude'] = split[1].astype(float)

#Drop the Location column from data frame
data = data[['Issue Date', 'Violation', 'Latitude', 'Longitude', 'Street']]

#Insert new columns into dataframe
data.insert(1, 'Issue_Date', '')
data.insert(2, 'Time', '')

#Go over all rows, and split Date and Time
for index, row in data.iterrows():
    date_time_str = row['Issue Date']

    date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y %I:%M:%S %p')

    # Extract date and time
    data.at[index, 'Issue_Date'] = date_time_obj.date()
    data.at[index, 'Time'] = date_time_obj.time()


#Drop the Issue Date column from data frame
data = data[['Issue_Date', 'Time', 'Violation', 'Latitude', 'Longitude', 'Street']]

#Rename columns
data.rename(columns = {'Violation':'Violation_Type', 'Street':'Street_Name'}, inplace = True)

data.insert(6, 'Street_Type', '')

#Go over all rows, and split street name and type
for index, row in data.iterrows():
    tokens = row['Street_Name'].split()

    if(len(tokens) == 1):
        data.at[index, 'Street_Name'] = tokens[0]
    else:
        # Reconstructing 'Street_Name' without the last token
        data.at[index, 'Street_Name'] = ' '.join(tokens[:-1])
        
        # Assigning the last token to 'Street_Type'
        data.at[index, 'Street_Type'] = tokens[-1]

print(data)
# #store it to csv
data.to_csv('Parking_Citation_Street.csv', index=False)

csv_file_path = 'Parking_Citation_Street.csv'

table_name = 'Parking_Citation'

street = pd.read_csv('Street.csv')
stret = street['Street_Name'].unique()
type = street['Street_Type'].unique()
print(stret)
print(type)

Ngh = pd.read_csv('Neighbourhood.csv')
Ngh = Ngh['Neighbourhood_Name'].unique()
print(Ngh)

# # Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

df['Neighbourhood_Name'] = [random.choice(Ngh) for _ in range(len(df))]

#Go over all rows, and split Date and Time
for index, row in df.iterrows():
    str = row['Street_Name']

    str = str.upper()
    df.at[index, 'Street_Name'] = str

# df = df[['Latitude', 'Longitude', 'Neighbourhood_Name', 'Street_Name', 'Street_Type']]

df = df[df['Street_Name'].isin(stret)]
df = df[df['Street_Type'].isin(type)]
df.to_csv('Parking_Citation_Street.csv', index=False)
#-------------------------------------------------------------------------

#--------------------------Parking Violation------------------------
data = pd.read_csv("Parking_Contravention__Citations.csv", dtype={6: object})

new_data = data[['Violation', 'Full Fine']]

#Remove dulpicate rows
data = new_data.drop_duplicates()

#Rename columns
data.rename(columns = {'Violation':'Violation_Type', 'Full Fine':'Fine_Amount'}, inplace = True)

df = data.dropna(subset=['Fine_Amount'])
df = df.dropna(subset=['Violation_Type'])

#store it to csv
df.to_csv('Parking_Violation.csv', index=False)
#-------------------------------------------------------------------------

#--------------------------Neighbourhood------------------------
data = pd.read_csv("Addresses.csv")

data = data[['Neighbourhood']]

#Calculate  number of houses in each neighbourhood
houses = data.value_counts()

# Converting to DataFrame and resetting index
data = houses.reset_index()

# Renaming columns
data.columns = ['Neighbourhood_Name', 'Number_Of_Houses']

# #store it to csv
data.to_csv('Neighbourhood.csv', index=False)
#-------------------------------------------------------------------------

#--------------------------WFPS_Call-----------------------
data = pd.read_csv("WFPS_Call_Logs.csv")

data = data[['Incident Number', 'Incident Type', 'Call Time', 'Neighbourhood']]

#Rename columns
data.rename(columns = {'Incident Number':'WFPS_Call_ID', 'Incident Type':'Reason', 'Neighbourhood':'Neighbourhood_Name'}, inplace = True)

#Insert new columns into dataframe
data.insert(1, 'Date', '')
data.insert(2, 'Call_Time', '')

#Go over all rows, and split Date and Time
for index, row in data.iterrows():
    date_time_str = row['Call Time']

    date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y %I:%M:%S %p')

    # Extract date and time
    data.at[index, 'Date'] = date_time_obj.date()
    data.at[index, 'Call_Time'] = date_time_obj.time()

#Drop the Call Time column from data frame
data = data[['WFPS_Call_ID', 'Date', 'Reason', 'Call_Time', 'Neighbourhood_Name']]

#store it to csv
data.to_csv('WFPS_Call.csv', index=False)

#All neighbourhoods
nhood = pd.read_csv('Neighbourhood.csv')

# Read the CSV file into a DataFrame
df = pd.read_csv("WFPS_Call.csv")
data = nhood["Neighbourhood_Name"].unique()  

df = df[df['Neighbourhood_Name'].isin(data)]
df.to_csv('WFPS_Call.csv', index=False)
#-------------------------------------------------------------------------

#--------------------------GPS Point-----------------------
data = pd.read_csv("Addresses.csv")

data = data[['Geometry', 'Street Name', 'Street Type', 'Neighbourhood']]

#Drop all rows with NaN value in latitide and longitude
data = data.dropna(subset=['Geometry'])

# Splitting the Location column and expanding into two columns
split = data['Geometry'].str.strip('()').str.split(', ', expand=True)

# Converting the new columns to float
data.loc[:,'Latitude'] = split[0].astype(float)
data.loc[:,'Longitude'] = split[1].astype(float)

#Drop the Location column from data frame
data = data[['Latitude', 'Longitude', 'Street Name', 'Street Type', 'Neighbourhood']]
data = data[["Latitude", "Longitude", "Neighbourhood", "Street Name", "Street Type"]]
data.columns = ["Latitude", "Longitude", "Neighbourhood_Name", "Street_Name", "Street_Type"]

data = data.dropna(subset=['Street_Type'])
data = data.dropna(subset=['Street_Name'])
data = data.dropna(subset=['Neighbourhood_Name'])
data = data.dropna(subset=['Latitude'])
data = data.dropna(subset=['Longitude'])

# #store it to csv
data.to_csv('GPS_Point.csv', index=False)
#-------------------------------------------------------------------------

#--------------------------Tow-----------------------
data = pd.read_csv("Rush_Hour_Vehicle_Towing_Data.csv")

data = data[['Request Date', 'Location Pickup', 'GPS Pickup', 'Status']]

#Drop all rows with NaN value in latitide and longitude
data = data.dropna(subset=['GPS Pickup'])

# Splitting the Location column and expanding into two columns
split = data['GPS Pickup'].str.strip('POINT ()').str.split(' ', expand=True)

# Converting the new columns to float
data.loc[:,'Longitude'] = split[0].astype(float)
data.loc[:,'Latitude'] = split[1].astype(float)

#Drop the GPS Point column from data frame
data = data[['Request Date', 'Status', 'Location Pickup', 'Latitude', 'Longitude']]

#Insert a new column into dataframe
data.insert(1, 'Street_Type', '')
data.insert(2, 'Street_Name', '')
data.insert(1, 'Date', '')
data.insert(2, 'Time', '')

#Go over all rows, and split street name and type, and time into date and time
for index, row in data.iterrows():
    tokens = row['Location Pickup'].split()

    if(len(tokens) == 1):
        data.at[index, 'Street_Name'] = tokens[0]
    else:
        # Reconstructing 'Street_Name' without the last token
        data.at[index, 'Street_Name'] = ' '.join(tokens[:-1])
        
        # Assigning the last token to 'Street_Type'
        data.at[index, 'Street_Type'] = tokens[-1]
    
    #Split Request date into date and time
    date_time_str = row['Request Date']

    date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y %I:%M:%S %p')

    # Extract date and time
    data.at[index, 'Date'] = date_time_obj.date()
    data.at[index, 'Time'] = date_time_obj.time()

#Drop processed columns from data frame
data = data[['Date', 'Time', 'Status', 'Street_Name', 'Street_Type', 'Latitude', 'Longitude']]

#Remove the direction
for index, row in data.iterrows():
    tokens = row['Street_Name'].split()
    temp = row['Street_Type']

    if(len(temp) == 1):
        data.at[index, 'Street_Name'] = tokens[0]
        data.at[index, 'Street_Type'] = tokens[1]

#Change street types to maintain consistency
dictionary = {'AVE': 'AVE', 'ST':'ST', 'HWY':'HWY', 'Ave.':'AVE', 'RD':'RD', 'CRES':'CRES', 
 'DR': 'DR', 'BLVD':'BLVD', 'St.':'ST', 'BAY':'BAY', 'PL':'PL', 'WAY':'WAY',
 'COVE':'COVE'}

for index, row in data.iterrows():
    type = row['Street_Type']
    data.at[index, 'Street_Type'] = dictionary[type]

for index, row in data.iterrows():
    str = row['Street_Name']

    str = str.upper()
    data.at[index, 'Street_Name'] = str

# #store it to csv
data.to_csv('Tow.csv', index=False)
#-------------------------------------------------------------------------

#--------------------------Street-----------------------
data = pd.read_csv("Addresses.csv")

data = data[['Street Name', 'Street Type']]

#Calculate  number of houses on each street
houses = data.value_counts()

# Converting to DataFrame and resetting index
data = houses.reset_index()

#Renaming columns
data.columns = ['Street_Name', 'Street_Type', 'Number_Of_Houses']

#store it to csv
data.to_csv('Street.csv', index=False)
#-------------------------------------------------------------------------

#------------------------Neighbourhood Street-----------------------------
data = pd.read_csv("Addresses.csv")

data = data[['Neighbourhood', 'Street Name', 'Street Type']]

#Remove duplicates
data = data.drop_duplicates()

#Renaming columns
data.columns = ['Neighbourhood_Name', 'Street Name', 'Street Type']

data = data.dropna(subset=['Street_Type'])
data = data.dropna(subset=['Neighbourhood_Name'])

#store it to csv
data.to_csv('Neighbourhood_Street.csv', index=False)
#-------------------------------------------------------------------------

#------------------------------Substances---------------------------------
data = pd.read_csv("Substance_Use.csv")
data = data[['Incident Number', 'Dispatch Date', 'Substance', 'Neighbourhood']]

#Drop all rows with NaN value in Neighbourhood
data = data.dropna(subset=['Neighbourhood'])

#Insert new columns into dataframe
data.insert(1, 'Date', '')
data.insert(2, 'Time', '')

#Go over all rows, and split Date and Time
for index, row in data.iterrows():
    date_time_str = row['Dispatch Date']

    date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y %I:%M:%S %p')

    # Extract date and time
    data.at[index, 'Date'] = date_time_obj.date()
    data.at[index, 'Time'] = date_time_obj.time()

#Drop the Call Time column from data frame
data = data[['Incident Number', 'Date', 'Time', 'Substance', 'Neighbourhood']]

#Rename columns
data.rename(columns = {'Incident Number':'Substance_Use_ID', 'Neighbourhood':'Neighbourhood_Name'}, inplace = True)

#store it to csv
data.to_csv('Substances.csv', index=False)

#All neighbourhoods
nhood = pd.read_csv('Neighbourhood.csv')

# Read the CSV file into a DataFrame
df = pd.read_csv("Substances.csv")
data = nhood["Neighbourhood_Name"].unique()  

df = df[df['Neighbourhood_Name'].isin(data)]
df.to_csv('Substances.csv', index=False)
#--------------------------------------------------------------------------

#--------------------------------Bus_Route---------------------------------
data_1 = pd.read_csv("Recent_Transit_On-Time_Performance_Data_20231019.csv")
data_2 = pd.read_csv("Recent_Transit_On-Time_Performance_Data.csv")

#Concatenate the two data frames
data = pd.concat([data_1, data_2], ignore_index=True)

#Remove dulpicate rows
data = data.drop_duplicates()

#Select specific columns from the data frame
data = data[['Route Number', 'Route Destination', 'Route Name']]

#Get all bus routes
data.drop_duplicates(subset=['Route Destination', 'Route Number'], inplace=True)

#Rename columns
data.rename(columns = {'Route Destination':'Route_Destination', 'Route Number':'Route_Number', 'Route Name':'Route_Name'}, inplace = True)

#store it to csv
data.to_csv('Bus_Route.csv', index=False)
#-------------------------------------------------------------------------

#------------------------------Bus_Stop------------------------------
data_1 = pd.read_csv("Recent_Transit_On-Time_Performance_Data_20231019.csv")
data_2 = pd.read_csv("Recent_Transit_On-Time_Performance_Data.csv")

#Concatenate the two data frames
data = pd.concat([data_1, data_2], ignore_index=True)

#Remove dulpicate rows
data = data.drop_duplicates()

#Select specific columns from the data frame
data = data[['Row ID', 'Stop Number', 'Scheduled Time', 'Deviation', 'Route Number', 'Route Destination', 'Location']]

#Get all bus routes
data.drop_duplicates(inplace=True)

#Drop all rows with NaN value in latitide and longitude
data = data.dropna(subset=['Location'])

# Splitting the Location column and expanding into two columns
split = data['Location'].str.strip('POINT ()').str.split(' ', expand=True)

# Converting the new columns to float
data.loc[:,'Longitude'] = split[0].astype(float)
data.loc[:,'Latitude'] = split[1].astype(float)

#Drop the Location column from data frame
data = data[['Row ID', 'Stop Number', 'Scheduled Time', 'Deviation', 'Route Number', 'Route Destination', 'Latitude', 'Longitude']]

#Rename columns
data.rename(columns = {'Route Destination':'Route_Destination', 'Route Number':'Route_Number', 'Row ID':'Row_ID', 
                       'Scheduled Time':'Scheduled_Time', 'Stop Number':'Bus_Stop_Number'}, inplace = True)

#Insert new columns into dataframe
data.insert(3, 'Date', '')


#Go over all rows, and split Date and Time
for index, row in data.iterrows():
    date_time_str = row['Scheduled_Time']

    date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y %I:%M:%S %p')

    # Extract date and time
    data.at[index, 'Date'] = date_time_obj.date()
    data.at[index, 'Scheduled_Time'] = date_time_obj.time()

#store it to csv
data.to_csv('Bus_Stop.csv', index=False)

#Select a sample of 1M rows
data = data.sample(1000000)

# Define the date range
start_date = datetime(2018, 7, 9)
end_date = datetime(2023, 11, 23)

# Generate random dates within the range
random_dates = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) for _ in range(1000000)]

# Assign these dates to a column in your DataFrame
data['Date'] = random_dates

data.to_csv('BusData.csv', index=False)
#-------------------------------------------------------------------------