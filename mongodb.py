from pymongo import MongoClient
from config.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["auto_message_bot"]
messages = db["messages"]

def add_message(data):
    return messages.insert_one(data).inserted_id

def get_all(chat_id):
    return list(messages.find({"chat_id": chat_id}))

def stop_message(msg_id):
    messages.update_one({"_id": msg_id}, {"$set": {"status": "stopped"}})
