from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import APIRouter


# MongoDB connection string
mongo_uri = "mongodb+srv://maheshdmah:Mahesh%40divya@cluster0.36cpwss.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)

# Connect to the database and collection
db = client["AMDVNextChat"]
collection = db["TEST"]

# Pydantic model for request body
class User(BaseModel):
    email: str
    password: str

# Create an APIRouter instance
router = APIRouter()

@router.post("/save/")
async def save_user(user: User):
    try:
        # Insert the user data into the collection
        result = collection.insert_one({"email": user.email, "password": user.password})
        if result.inserted_id:
            return {"message": "User data saved successfully"}
        else:
            raise HTTPException(status_code=500, detail="Failed to save user data")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))