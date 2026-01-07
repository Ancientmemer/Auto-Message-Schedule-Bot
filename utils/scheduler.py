import asyncio
import time
from pymongo import MongoClient
from config.config import MONGO_URI

mongo = MongoClient(MONGO_URI)
db = mongo["auto_message_bot"]
collection = db["schedules"]

async def schedule_loop(bot):
    print("⏰ Scheduler started")

    while True:
        now = int(time.time())

        for item in collection.find({
            "sent": False,
            "time": {"$lte": now}
        }):
            try:
                await bot.send_message(
                    chat_id=item["chat_id"],
                    text=item["text"],
                    reply_markup=item.get("buttons")
                )

                collection.update_one(
                    {"_id": item["_id"]},
                    {"$set": {"sent": True}}
                )

                print(f"✅ Message sent: {item['_id']}")

            except Exception as e:
                print("❌ Scheduler error:", e)

        await asyncio.sleep(2)
