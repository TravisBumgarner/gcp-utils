import base64
import os
import http.client
import urllib
import json

from dotenv import load_dotenv

load_dotenv()

PUSHOVER_API_KEY = os.environ.get('PUSHOVER_API_KEY')
PUSHOVER_USER_KEY = os.environ.get('PUSHOVER_USER_KEY')

def send(message):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": PUSHOVER_API_KEY,
                     "user": PUSHOVER_USER_KEY,
                     "message": message,
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    r = conn.getresponse()
    return r


def gcp_billing_alert(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    try:
        pubsub_message = base64.b64decode(event['data']).decode('utf-8')
        loaded_json = json.loads(pubsub_message)
        percent_of_budget = float(loaded_json['costAmount']) / float(loaded_json['budgetAmount'])
        if percent_of_budget > 0.8:
            send(f'Almost time to panic {percent_of_budget}')
    except:
        send('pubsub billing failure on GCP PANIC!')
    