import os
import threading
import asyncio
from http.server import BaseHTTPRequestHandler, HTTPServer
from pyrogram import Client, idle

from config.config import BOT_TOKEN, API_ID, API_HASH

from handlers.start import register_start_handler
from handlers.add import register_add_handlers
from handlers.stop import register_stop_handlers
from handlers.status import register_status_handlers
from handlers.broadcast import register_broadcast_handlers
from utils.scheduler import schedule_loop

# ========== Telegram Bot ==========
app = Client(
    "AutoMessageBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register handlers
register_start_handler(app)
register_add_handlers(app)
register_stop_handlers(app)
register_status_handlers(app)
register_broadcast_handlers(app)


async def main():
    await app.start()
    print("🤖 Bot started and listening")

    # run scheduler in background (NON-BLOCKING)
    asyncio.create_task(schedule_loop(app))

    await idle()
    await app.stop()


if __name__ == "__main__":
    asyncio.run(main())
