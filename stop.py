from pyrogram import filters
from database.mongodb import get_all, stop_message
from utils.admin_check import is_admin

def register_stop_handlers(app):
    @app.on_message(filters.command("stop") & filters.group)
    async def stop(_, message):
        if not await is_admin(_, message):
            return
        msgs = get_all(message.chat.id)
        for m in msgs:
            stop_message(m["_id"])
        await message.reply("🛑 All messages stopped")
