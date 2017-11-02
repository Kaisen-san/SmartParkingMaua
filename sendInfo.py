# Import libraries
import requests
import time
import configparser

def Post(action):
    # Initialize INI file
    config = configparser.ConfigParser()
    config.read('LocalInfo.INI')

    # Set post URL
    r = requests.post('http://httpbin.org/post', json={"key": "value"})
    #print(r.status_code)

    # Set JSON variables
    timestamp = int(time.time())
    gate = config['Local']['gate']

    # Send information
    r.json()
    {
        "timestamp": timestamp,
        "action": action,
        "portao": gate
    }
