# for firestore trigger to check logs

import functions_framework
import json
 
@functions_framework.cloud_event
def on_user_create_arun(cloud_event):
    """
    Cloud Functions Gen 2
    Triggered when a Firestore document is CREATED
    Database: arundb
    Collection: users
    """
 
    # Raw Firestore event payload
    data = cloud_event.data or {}
 
    # Firestore document data
    value = data.get("value", {})
    fields = value.get("fields", {})
 
    def get_string(field):
        return fields.get(field, {}).get("stringValue")
 
    def get_int(field):
        val = fields.get(field, {}).get("integerValue")
        return int(val) if val is not None else None
 
    # Extract fields safely
    name = get_string("name")
    email = get_string("email")
    role = get_string("role")
    exp = get_int("exp")
 
    # Structured logs (best practice)
    print("FIRESTORE CREATE EVENT RECEIVED ")
    print(json.dumps({
        "document": value.get("name"),
        "name": name,
        "email": email,
        "role": role,
        "exp": exp
    }, indent=2))
 
   # Optional: business logic placeholder
