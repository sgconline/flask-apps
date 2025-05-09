"""
model.py
--------
Connection details to mongodb backup database
"""
import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import abort
from dotenv import load_dotenv
load_dotenv()

# # Retrieve MongoDB credentials from environment variables or use defaults
# mdb_admin = os.getenv("mdb_user")
# mdb_pword = os.getenv("mdb_pword")
# mdb_host  = os.getenv("mdb_host")
# mdb_port  = os.getenv("mdb_port")
# mdb_name = os.getenv("mdb_db")

# MongoDB connection setup with dynamic user and password
#mongo_uri = os.getenv("MONGO_URI", "mongodb://mdbadmin:mdbadmin@contacts-mdb:27017")
mongo_uri = os.getenv("mdb_conn_str")
database_name = os.getenv("mdb_db")

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
contacts_collection = db[os.getenv("mdb_collection")]

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
