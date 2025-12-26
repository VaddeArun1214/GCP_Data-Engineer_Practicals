from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.cloud import firestore

app = FastAPI(title="FastAPI Firestore CRUD")

# ---------------------------
# Firestore Client
# ---------------------------
db = firestore.Client(database="arundb")
users_ref = db.collection("users")


# ---------------------------
# Data Model
# ---------------------------
class User(BaseModel):
    name: str
    email: str
    role: str
    age: int


# ---------------------------
# CREATE USER
# ---------------------------
@app.post("/users")
def create_user(user: User):
    try:
        doc_ref = users_ref.document()
        doc_ref.set(user.dict())

        return {
            "message": "User created successfully",
            "id": doc_ref.id,
            "user": user
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------
# READ ALL USERS
# ---------------------------
@app.get("/users")
def get_all_users():
    try:
        docs = users_ref.stream()
        users = []

        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            users.append(data)

        return {
            "count": len(users),
            "users": users
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------
# READ SINGLE USER
# ---------------------------
@app.get("/users/{user_id}")
def get_user(user_id: str):
    doc = users_ref.document(user_id).get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="User not found")

    data = doc.to_dict()
    data["id"] = doc.id
    return data


# ---------------------------
# UPDATE USER
# ---------------------------
@app.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    doc_ref = users_ref.document(user_id)

    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="User not found")

    doc_ref.update(user.dict())

    return {
        "message": "User updated successfully",
        "id": user_id,
        "user": user
    }


# ---------------------------
# DELETE USER
# ---------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    doc_ref = users_ref.document(user_id)

    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="User not found")

    doc_ref.delete()

    return {
        "message": "User deleted successfully",
        "id": user_id
    }