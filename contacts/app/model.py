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

# Retrieve MongoDB credentials from environment variables or use defaults
mdb_admin = os.getenv("MDB_USER", "mdbadmin")
mdb_pword = os.getenv("MDB_PWORD", "mdbadmin")
mdb_host  = os.getenv("MDB_HOST", "contacts-mdb")
mdb_port  = os.getenv("MDB_PORT", "27017")
mdb_name = os.getenv("MDB_NAME", "contacts_db")
mdb_connection_str = os.getenv("MDB_CONNECTION_STR", "mongodb://" + mdb_admin + ":" + mdb_pword + "@" + mdb_host + ":" + mdb_port)

# MongoDB connection setup with dynamic user and password
mongo_uri = os.getenv("MONGO_URI", "mongodb://mdbadmin:mdbadmin@contacts-mdb:27017")
database_name = os.getenv("DATABASE_NAME", "contacts_db")

#mongo_uri = os.getenv(
#    "MONGO_URI",
#    f"mongodb://{mdb_admin}:{mdb_pword}@{mdb_host}:{mdb_port}/?authSource={mdb_name}"
#)
# MongoDB connection setup
#mongo_uri = os.getenv("MONGO_URI", "mongodb://" + mdb_connection_str)

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
