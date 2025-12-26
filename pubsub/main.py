# to reflect in pubsub and see logs in function app

import functions_framework
import base64
import json
 
@functions_framework.cloud_event
def consume_pubsub_arun(cloud_event):
    msg = cloud_event.data["message"]
 
    data = base64.b64decode(msg["data"]).decode("utf-8")
 
    print("PUBSUB MESSAGE RECEIVED")
    print(json.loads(data))
