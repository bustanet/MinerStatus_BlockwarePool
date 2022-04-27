# Import the following modules
import requests
import json
import os

# Variables
TOKEN = os.getenv("PUSH_API")

# Function to send Push Notification 
def notify(title, body):
 
    #TOKEN = 'Your Access Token'  # Pass your Access Token here
    # Make a dictionary that includes, title and body
    msg = {"type": "note", "title": title, "body": body}
    # Sent a posts request
    resp = requests.post('https://api.pushbullet.com/v2/pushes',
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:  # Check if fort message send with the help of status code
        raise Exception('Error', resp.status_code)
    else:
        print('Message sent')
 
#TOKEN = os.getenv("PUSH_API")
#pushbullet_noti("Hey", "How you doing?")