# Import libraries
import requests
import time
import configparser

minPrecision = 0.7

def ValidatePost(action, score):
    # Check if the current action is different than "others" classification
    if (action != "others"):
        # Check if the current score is higher than the minimum acceptable precision
        if (score > minPrecision):
            Post(action)

def Post(action):
    # Initialize INI file
    config = configparser.ConfigParser()
    config.read('localInfo.ini')

    # Set post URL
    r = requests.post('http://localhost/spmp', json={"key": "value"})
    #print(r.status_code)

    # Set JSON variables
    timestamp = int(time.time())
    gate = config['Local']['Gate']

    # Send information
    r.json()
    {
        "timestamp": timestamp,
        "action": action,
        "gate": gate
    }
