# for storage bucket 

import functions_framework
 
 
@functions_framework.cloud_event
def on_file_upload_arun(cloud_event):
    data = cloud_event.data or {}
 
    bucket = data.get("bucket")
    name = data.get("name")
    size = data.get("size")
    content_type = data.get("contentType")
 
    print("CLOUD STORAGE EVENT RECEIVED")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Size: {size} bytes")
    print(f"Content Type: {content_type}")