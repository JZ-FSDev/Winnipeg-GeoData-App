import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np

def update_map(df, text_column, dual_markers=False):
    # Create a scatter plot on a map with markers

    # Define the size of the markers
    df['size'] = 10

    # Create a scatter map using plotly.graph_objects
    fig = go.Figure()

    first_prefix = ""
    second_prefix = ""

    if dual_markers:
        # Add scatter mapbox trace wiht multiple text per marker
        first_prefix = text_column[0].split('_')[0]
        second_prefix = text_column[1].split('_')[0]

        fig.add_trace(
            go.Scattermapbox(
                lat=df[first_prefix + '_Latitude'],
                lon=df[first_prefix + '_Longitude'],
                mode='markers',
                marker=dict(
                    size=df['size'],
                ),
                text=f"{text_column[0]} = " + df[text_column[0]].astype(str),
                name=text_column[0],
            )
        )
        fig.add_trace(
            go.Scattermapbox(
                lat=df[second_prefix + '_Latitude'],
                lon=df[second_prefix + '_Longitude'],
                mode='markers',
                marker=dict(
                    size=df['size'],
                ),
                text=f"{text_column[1]} = " + df[text_column[1]].astype(str),
                name=text_column[1],
            )
        )
    elif isinstance(text_column, list):
        text = ''
        for string in text_column:
            text += f"{string} = " + df[string].astype(str)
            text += '  '

        # Add scatter mapbox trace wiht multiple text per marker
        fig.add_trace(
            go.Scattermapbox(
                lat=df['Latitude'],
                lon=df['Longitude'],
                mode='markers',
                marker=dict(
                    size=df['size'],
                ),
                text=text,
            )
        )
    else:
        # Add scatter mapbox trace
        fig.add_trace(
            go.Scattermapbox(
                lat=df['Latitude'],
                lon=df['Longitude'],
                mode='markers',
                marker=dict(
                    size=df['size'],
                ),
                text=f"{text_column} = " + df[text_column].astype(str),
            )
        )

    if dual_markers:
        first_latitudes = df[first_prefix + '_Latitude'].tolist()
        second_latitudes = df[second_prefix + '_Latitude'].tolist()

        second_longitudes = df[first_prefix + '_Longitude'].tolist()
        second_longitudes = df[second_prefix + '_Longitude'].tolist()

        # Concatenate the lists
        merged_latitudes = np.concatenate([first_latitudes, second_latitudes])
        merged_longitudes = np.concatenate([second_longitudes, second_longitudes])

        # Calculate the mean
        merged_mean_lat = np.mean(merged_latitudes)
        merged_mean_lon = np.mean(merged_longitudes)

        # Set map layout
        fig.update_layout(
            mapbox=dict(
                style='open-street-map',
                center=dict(
                    lat=merged_mean_lat,
                    lon=merged_mean_lon,
                ),
                zoom=10,
            ),
            height=550,
        )
    else:
        # Set map layout
        fig.update_layout(
            mapbox=dict(
                style='open-street-map',
                center=dict(
                    lat=df['Latitude'].mean(),
                    lon=df['Longitude'].mean(),
                ),
                zoom=10,
            ),
            height=550,
        )

    # Save the interactive map as an HTML file
    pio.write_html(fig, file='static/interactive_map.html', auto_open=False)


def update_empty_map():
    # Create an empty map centered at the middle of Winnipeg

    # Winnipeg coordinates
    winnipeg_lat = 49.8951
    winnipeg_lon = -97.1384

    # Create a DataFrame with a single row for Winnipeg coordinates
    df = pd.DataFrame({
        'Latitude': [winnipeg_lat],
        'Longitude': [winnipeg_lon]
    })

    # Create a scatter map using plotly.graph_objects
    fig = go.Figure()


    # Add scatter mapbox trace
    fig.add_trace(
        go.Scattermapbox(
            lat=df['Latitude'],
            lon=df['Longitude'],
            mode='markers',
            marker=dict(
                opacity=0  # Set opacity to 0 for an invisible data point
            ),
            hoverinfo='skip'  # Disable hoverinfo for this trace
        )
    )

    # Set map layout
    fig.update_layout(
        mapbox=dict(
            style='open-street-map',
            center=dict(
                lat=df['Latitude'].mean(),
                lon=df['Longitude'].mean(),
            ),
            zoom=10,
        ),
        height=550,
    )

    # Save the interactive map as an HTML file
    pio.write_html(fig, file='static/interactive_map.html', auto_open=False)