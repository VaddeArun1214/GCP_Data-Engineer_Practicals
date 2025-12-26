from google.cloud import firestore

db = firestore.Client(database="arundb")

# Create
doc_ref = db.collection('users').add({
    'name': ' Ram',
    'email': 'Ram@example.com',
    'role': 'Hr',
    'age': 7
})

# Read
print("Users age >= 25")
for doc in db.collection('users').where('age', '>=', 26).stream():
    print(f'{doc.id} => {doc.to_dict()}')

# Update
db.collection('users').document(doc_ref[1].id).update({
   'age': 32
})
print(f"Updated user {doc_ref[1].id} age to 32")

# Delete Anjani by email 
query = db.collection('users').where('email', '==', 'vaddearun479@example.com')

for doc in query.stream():
    db.collection('users').document(doc.id).delete()
    print(f"Deleted Arun record: {doc.id}")