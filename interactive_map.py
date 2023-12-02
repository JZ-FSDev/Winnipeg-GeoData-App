import pandas as pd
import plotly.express as px
import numpy as np
import plotly.offline as offline


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
    offline.plot(fig, filename='templates/interactive_map.html', auto_open=False)