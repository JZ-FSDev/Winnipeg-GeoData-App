CREATE INDEX idx_bus_stop_coordinates ON Bus_Stop (Latitude, Longitude);
CREATE INDEX idx_bus_stop_route ON Bus_Stop (Route_Number, Route_Destination);
CREATE INDEX idx_bus_stop_time_date ON Bus_Stop (Scheduled_Time, Date);

CREATE INDEX idx_gps_coordinates ON GPS_Point (Latitude, Longitude);
CREATE INDEX idx_street ON GPS_Point (Street_Name, Street_Type);
CREATE INDEX idx_neighbourhood on GPS_Point (Neighbourhood_Name);