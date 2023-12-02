import math

def meters_to_latitude_difference(distance_meters):
    # Earth's radius in meters
    earth_radius = 6371000

    # Convert distance to radians
    angular_distance = distance_meters / earth_radius

    # Calculate the difference in latitude
    latitude_difference = math.degrees(angular_distance)
    
    return latitude_difference


def meters_to_longitude_difference(distance_meters, latitude):
    # Earth's radius in meters
    earth_radius = 6371000

    # Convert distance to radians
    angular_distance = distance_meters / earth_radius

    # Calculate the difference in longitude
    longitudinal_conversion = math.cos(math.radians(latitude))
    longitude_difference = math.degrees(angular_distance) / longitudinal_conversion

    return longitude_difference
