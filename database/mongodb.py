from pymongo import MongoClient
from config.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["auto_scheduler"]
collection = db["messages"]


def add_message(data):
    collection.insert_one(data)


def get_all(chat_id):
    return list(collection.find({"chat_id": chat_id, "status": "running"}))


def get_all_running():
    return list(collection.find({"status": "running"}))


def stop_message(msg_id):
    collection.update_one(
        {"_id": msg_id},
        {"$set": {"status": "stopped"}}
    )


def update_last_sent(msg_id, timestamp):
    collection.update_one(
        {"_id": msg_id},
        {"$set": {"last_sent": timestamp}}
    )
