# Import libraries
import requests
import time
import configparser


# Set minimum precision for post validation
minPrecision = 0.7


def ValidatePost(action, score):
    # Check if the current action is different than "others" classification
    if ((action == "entrance") or (action == "exit")):
        # Check if the current score is higher than the minimum acceptable precision
        if (score > minPrecision):
            Post(action)
        else:
            print("Image score is lower than the minimum precision (%.2f)" % minPrecision)


def Post(action):
    # Initialize INI file
    config = configparser.ConfigParser()
    config.read('localInfo.ini')
    
    # Set JSON variables
    timestamp = int(time.time())
    gate = config['Local']['Gate']

    # Send information
    url = 'https://smartparkingmaua.000webhostapp.com/'
    payload = {
        "timestamp": timestamp,
        "action": action,
        "gate": gate
    }

    # Set post URL
    r = requests.post(url, json=payload)
    print("Post status: %i" % r.status_code)
