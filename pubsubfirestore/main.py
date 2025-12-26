# to send a single document reflects to firestore automatically

import base64
import json
from google.cloud import firestore
from datetime import datetime

# Firestore client
db = firestore.Client(database="arundb")

def consume_pubsub_arun(event, context):
    """
    Triggered from a Pub/Sub message
    """

    # Decode Pub/Sub message
    message = base64.b64decode(event['data']).decode('utf-8')
    payload = json.loads(message)

    # Prepare Firestore log document
    log_data = {
        "event": payload.get("event"),
        "user": payload.get("user"),
        "received_at": datetime.utcnow(),
        "source": "pubsub",
        "topic": context.resource["name"]
    }

    # Store in Firestore (NoSQL)
    db.collection("user_activity_logs").add(log_data)

    print("Log stored in Firestore:", log_data)



# to send multiple documents to firestore automatically

# import base64
# import json
# from google.cloud import firestore
# from datetime import datetime

# db = firestore.Client(database="arundb")

# def consume_pubsub_arun(event, context):

#     message = base64.b64decode(event['data']).decode('utf-8')
#     payload = json.loads(message)

#     event_type = payload.get("event")
#     users = payload.get("users", [])

#     batch = db.batch()

#     for user in users:
#         doc_ref = db.collection("user_activity_logs").document()
#         batch.set(doc_ref, {
#             "event": event_type,
#             "user": user,
#             "received_at": datetime.utcnow(),
#             "source": "pubsub",
#             "topic": context.resource["name"]
#         })

#     batch.commit()
#     print(f"{len(users)} users inserted into Firestore")