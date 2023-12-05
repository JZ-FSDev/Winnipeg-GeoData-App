# Winnipeg-GeoData-App

## Running Instructions

**Project must be ran on Windows OS as the ODBC required by the webserver is {SQL Server}** 

### Dependencies:
Any version of the dependencies below should suffice with preference over later versions
- pandas
- plotly.express
- numpy as np
- plotly.offline
- pymssql


0. Ensure that the username and password are valid to access uranium.cs.umanitoba.ca, and port is not being accessed locally.  Make any changes if neccessary (localhost is fine for the host)
1. Start up the webserver by running `python webserver.py` (Database will populate as the webserver boots up)
2. Access the application on the browser by visiting `localhost:port` (where `port` is the port from step *0.*) on Google Chrome when the webserver prints on console that it is ready
3. 