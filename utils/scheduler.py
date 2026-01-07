import asyncio
import time
from database.mongodb import collection

async def schedule_loop(app):
    print("⏰ Scheduler started")

    while True:
        for item in collection.find({"status": "running"}):
            try:
                await app.send_message(
                    chat_id=item["chat_id"],
                    text=item["text"]
                )

                await asyncio.sleep(item["interval"])

            except Exception as e:
                print("❌ Scheduler error:", e)

        await asyncio.sleep(2)
