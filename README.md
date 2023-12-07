# Winnipeg-GeoData-App

**Project must be ran on Windows OS to avoid any compatibility conflicts** 

## Dependencies:
Install the dependencies required to run the project by calling the following on a terminal that is pointed to the directory of this README:
`pip install -r dependencies.txt`

If the above method does not work, manually install the following dependencies by calling: 
`pip install X` where `X` is each of the packages below
- pandas
- plotly
- numpy
- flask
- pymssql


## Running Instructions
1. Ensure all dependencies defined above are installed successfully
2. Ensure that the `username` and `password` defined in `config.cfg` are valid to access uranium.cs.umanitoba.ca, and the `port` is not in use locally.  The existing username and password is known to be able to connect to the MSSQL server successfully.  Make changes to these values if necessary.
3. If the database needs to be repopulated upon bootup of the program, call: `python webserver.py -populate`.  Otherwise, if the webserver is ran with the default username and password, the database is already fully populated and the webserver can be started while skipping the database population by calling: `python webserver.py`
4. Access the application on a web browser (ideally Chrome) by visiting `localhost:port` (where `port` is the port defined in the `config.cfg`) after the webserver prints on console `* Running on http://localhost:[port]`