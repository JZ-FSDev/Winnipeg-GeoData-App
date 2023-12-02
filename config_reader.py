

config_file = "config.cfg"  # Config file containing the host and port

def get_username_password():
    credentials = {}

    try:
        with open(config_file) as f:
            for line in f:
                key, value = map(str.strip, line.split('=', 1))
                credentials[key] = value
    except FileNotFoundError:
        print("Could not find config file.")
        exit(1)
    except ValueError:
        print("Invalid config file format.")
        exit(1)

    # Extract username and password
    username = credentials.get('username')
    password = credentials.get('password')

    if username is None or password is None:
        print("Username or password not provided.")
        exit(1)
    else:
        return username, password


# Reads the config file and returns the host and port
def get_host_port():
    credentials = {}

    try:
        with open(config_file) as f:
            for line in f:
                key, value = map(str.strip, line.split('=', 1))
                credentials[key] = value
    except FileNotFoundError:
        print("Could not find config file.")
        exit(1)
    except ValueError:
        print("Invalid config file format.")
        exit(1)

    # Extract username and password
    host = credentials.get('host')
    port = credentials.get('port')

    if host is None or port is None:
        print("Host or port not provided.")
        exit(1)
    else:
        return host, int(port)