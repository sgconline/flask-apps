"""
model.py
--------
Connection details to mongodb backup database
"""

import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import abort

# MongoDB connection setup
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
database_name = os.getenv("DATABASE_NAME", "contacts_db")
try:
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    # Force connection on a request as the
    # connect=True parameter of MongoClient seems
    # to be useless here
    client.server_info()
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    raise

db = client[database_name]
contacts_collection = db["contacts"]

def get_all_contacts():
    contacts = list(contacts_collection.find())
    for contact in contacts:
        contact["_id"] = str(contact["_id"])
    return contacts

def get_contact(contact_id):
    contact = contacts_collection.find_one({"_id": ObjectId(contact_id)})
    if contact:
        contact["_id"] = str(contact["_id"])
    return contact

def add_contact(data):
    result = contacts_collection.insert_one(data)
    return str(result.inserted_id)

def update_contact(contact_id, data):
    result = contacts_collection.update_one(
        {"_id": ObjectId(contact_id)}, {"$set": data}
    )
    return result.matched_count > 0

def delete_contact(contact_id):
    try:
        result = contacts_collection.delete_one({"_id": ObjectId(contact_id)})
    except Exception as e:
        print(f"Error deleting contact: {e}")
        return False