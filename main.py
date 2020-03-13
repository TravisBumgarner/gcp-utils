import base64
import os
import http.client
import urllib

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
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    send(pubsub_message)
    print(pubsub_message)

    