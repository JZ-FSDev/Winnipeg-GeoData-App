--Data acquired from : 
--https://data.winnipeg.ca/

use cs3380;

DROP TABLE IF EXISTS Parking_Citation;
DROP TABLE IF EXISTS Parking_Violation;
DROP TABLE IF EXISTS Paystation;
DROP TABLE IF EXISTS WFPS_Call;
DROP TABLE IF EXISTS Substance_Use;
DROP TABLE IF EXISTS Lane_Closure;
DROP TABLE IF EXISTS Tow;
DROP TABLE IF EXISTS Bus_Stop;
DROP TABLE IF EXISTS Bus_Route;
DROP TABLE IF EXISTS GPS_Point;
DROP TABLE IF EXISTS Neighbourhood_Street;
DROP TABLE IF EXISTS Street;
DROP TABLE IF EXISTS Neighbourhood;


CREATE TABLE Neighbourhood (
    Neighbourhood_Name VARCHAR(255) NOT NULL,
    Number_OF_Houses INT,
    PRIMARY KEY (Neighbourhood_Name)
);

CREATE TABLE Street (
    Street_Name VARCHAR(255) NOT NULL,
    Street_Type VARCHAR(50),
    Number_Of_Houses INT,
    PRIMARY KEY (Street_Name, Street_Type)
);

CREATE TABLE Neighbourhood_Street (
    Neighbourhood_Name VARCHAR(255) NOT NULL,
    Street_Name VARCHAR(255) NOT NULL,
    Street_Type VARCHAR(50) NOT NULL,
    PRIMARY KEY (Neighbourhood_Name, Street_Name, Street_Type),
    FOREIGN KEY (Street_Name, Street_Type) REFERENCES Street(Street_Name, Street_Type),
    FOREIGN KEY (Neighbourhood_Name) REFERENCES Neighbourhood(Neighbourhood_Name) 
);

CREATE TABLE WFPS_Call(
    WFPS_Call_ID BIGINT NOT NULL,
    Date DATE,
    Reason VARCHAR(100), 
    Call_Time TEXT,
    Neighbourhood_Name VARCHAR(255),
    FOREIGN KEY (Neighbourhood_Name) REFERENCES Neighbourhood(Neighbourhood_Name) 
);

CREATE TABLE Substance_Use(
    Substance_Use_ID INT NOT NULL,
    Date DATE, 
    Time TIME,
    Substance VARCHAR(100),
    Neighbourhood_Name VARCHAR(255),
    FOREIGN KEY (Neighbourhood_Name) REFERENCES Neighbourhood(Neighbourhood_Name) 
);

CREATE TABLE GPS_Point (
    Latitude DECIMAL(11,8),
    Longitude DECIMAL(11,8),
    Neighbourhood_Name VARCHAR(255),
    Street_Name VARCHAR(255),
    Street_Type VARCHAR(50),
    PRIMARY KEY (Longitude, Latitude),
    FOREIGN KEY (Street_Name, Street_Type) REFERENCES Street(Street_Name, Street_Type),
    FOREIGN KEY (Neighbourhood_Name) REFERENCES Neighbourhood(Neighbourhood_Name) 
);

CREATE TABLE Paystation (
    Paystation_ID INT NOT NULL,
    Time_Limit INT,
    Space INT,
    Longitude DECIMAL(11,8),
    Latitude DECIMAL(11,8),
    Street_Name VARCHAR(255),
    Street_Type VARCHAR(50),
    PRIMARY KEY (Paystation_ID),
    FOREIGN KEY (Street_Name, Street_Type) REFERENCES Street(Street_Name, Street_Type),
    FOREIGN KEY (Longitude, Latitude) REFERENCES GPS_Point(Longitude, Latitude)
);

CREATE TABLE Parking_Violation (
    Violation_Type VARCHAR(255) NOT NULL,
    Fine_Amount DECIMAL(10,2),
    PRIMARY KEY (Violation_Type)
);

CREATE TABLE Parking_Citation (
    Citation_ID INT NOT NULL,
    Issue_Date DATE,
    Time TIME,
    Violation_Type VARCHAR(255),
    Longitude DECIMAL(11,8),
    Latitude DECIMAL(11,8),
    PRIMARY KEY (Citation_ID),
    FOREIGN KEY (Longitude, Latitude) REFERENCES GPS_Point(Longitude, Latitude),
    FOREIGN KEY (Violation_Type) REFERENCES Parking_Violation(Violation_Type)
);

CREATE TABLE Lane_Closure (
    Lane_Closure_ID INT NOT NULL,
    Date_To DATE,
    Date_From DATE,
    Street_Name VARCHAR(255),
    Street_Type VARCHAR(50),
    Longitude DECIMAL(11,8),
    Latitude DECIMAL(11,8),
    PRIMARY KEY (Lane_Closure_ID),
    FOREIGN KEY (Longitude, Latitude) REFERENCES GPS_Point(Longitude, Latitude),
    FOREIGN KEY (Street_Name, Street_Type) REFERENCES Street(Street_Name, Street_Type)
);

CREATE TABLE Tow (
    Tow_ID INT NOT NULL,
    Date DATE,
    Time TIME,
    Status VARCHAR(50),
    Street_Name VARCHAR(255),
    Street_Type VARCHAR(50),
    Longitude DECIMAL(11,8),
    Latitude DECIMAL(11,8),
    PRIMARY KEY (Tow_ID),
    FOREIGN KEY (Longitude, Latitude) REFERENCES GPS_Point(Longitude, Latitude),
    FOREIGN KEY (Street_Name, Street_Type) REFERENCES Street(Street_Name, Street_Type)
);

CREATE TABLE Bus_Route (
    Route_Number VARCHAR(50) NOT NULL,
    Route_Destination VARCHAR(100) NOT NULL,
    Route_Name VARCHAR(100),
    PRIMARY KEY (Route_Number, Route_Destination)
);

CREATE TABLE Bus_Stop (
    Row_ID INT NOT NULL,
    Bus_Stop_Number INT NOT NULL,
    Scheduled_Time TIME,
    Date DATE,
    Deviation INT,
    Route_Number VARCHAR(50),
    Route_Destination VARCHAR(100),
    Longitude DECIMAL(11,8),
    Latitude DECIMAL(11,8),
    PRIMARY KEY (Row_ID),
    FOREIGN KEY (Longitude, Latitude) REFERENCES GPS_Point(Longitude, Latitude),
    FOREIGN KEY (Route_Number, Route_Destination) REFERENCES Bus_Route(Route_Number, Route_Destination)
);
