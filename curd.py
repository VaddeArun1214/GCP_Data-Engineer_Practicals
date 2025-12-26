from google.cloud import firestore
from datetime import datetime, timedelta
import random

# -------------------------------------------------
# Project Configuration
# -------------------------------------------------
PROJECT_ID = "samproject"   # GCP Project ID
LOGICAL_DB = "arun-nosql"   # Logical database (collection-level)
SUB_COLLECTION = "user_activity_logs"

# -------------------------------------------------
# Initialize Firestore Client (Native mode)
# -------------------------------------------------
db = firestore.Client(project=PROJECT_ID)

# Path:
# arun-nosql -> logs -> user_activity_logs
collection_ref = (
    db.collection(LOGICAL_DB)
      .document("logs")
      .collection(SUB_COLLECTION)
)

# -------------------------------------------------
# Sample Data
# -------------------------------------------------
users = [f"U{1000+i}" for i in range(50)]

activities = [
    "product_click",
    "view_page",
    "add_to_cart",
    "remove_from_cart",
    "wishlist_add",
    "search",
    "checkout_start"
]

products = [
    "iphone15", "samsung_s24", "macbook_air", "dell_xps",
    "airpods_pro", "sony_headphones", "ipad_pro", "pixel_8",
    "oneplus_12", "boat_earbuds", "nike_shoes", "adidas_shoes",
    "apple_watch", "fitbit_charge", "canon_dslr"
]

categories = [
    "electronics",
    "mobiles",
    "laptops",
    "accessories",
    "fashion",
    "fitness",
    "cameras"
]

devices = ["mobile", "desktop", "tablet"]

# -------------------------------------------------
# Insert Data using Batch
# -------------------------------------------------
batch = db.batch()
start_time = datetime.utcnow() - timedelta(days=1)

for i in range(200):
    doc_ref = collection_ref.document()
    product = random.choice(products)

    data = {
        "user_id": random.choice(users),
        "activity_type": random.choice(activities),
        "category": random.choice(categories),
        "product": product,
        "page": f"/product/{product}",
        "device": random.choice(devices),
        "timestamp": start_time + timedelta(seconds=i * random.randint(1, 5))
    }

    batch.set(doc_ref, data)

batch.commit()

print("✅ Inserted 200 records into Firestore")
print("📍 Path: samproject → arun-nosql → logs → user_activity_logs")
