from pyrogram import filters
from database.mongodb import get_all, stop_message
from utils.admin_check import is_admin

def register_stop_handlers(app):

    @app.on_message(filters.command("stop") & (filters.group))
    async def stop(client, message):

        if not await is_admin(client, message):
            return

        msgs = get_all(message.chat.id)
        if not msgs:
            return await message.reply("❌ No scheduled messages")

        for m in msgs:
            stop_message(m["_id"])

        await message.reply(f"🛑 Stopped {len(msgs)} messages")
