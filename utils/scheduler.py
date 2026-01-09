import asyncio
import time
from database.mongodb import get_all_running, update_last_sent

async def schedule_loop(app):
    print("⏰ Scheduler started")

    while True:
        now = int(time.time())
        msgs = get_all_running()

        for m in msgs:
            if now - m.get("last_sent", 0) >= m["interval"]:
                try:
                    await app.send_message(
                        chat_id=m["chat_id"],
                        text=m["text"]
                    )
                    update_last_sent(m["_id"], now)
                except Exception as e:
                    print("Scheduler error:", e)

        await asyncio.sleep(2)
