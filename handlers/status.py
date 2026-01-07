from pyrogram import filters
from database.mongodb import get_all
from utils.admin_check import is_admin

def register_status_handlers(app):
    @app.on_message(filters.command("status") & filters.group)
    async def status(_, message):
        if not await is_admin(_, message):
            return

        msgs = get_all(message.chat.id)
        if not msgs:
            return await message.reply("❌ No scheduled messages")

        text = "📊 Status List:\n"
        for i, m in enumerate(msgs, 1):
            text += f"{i}. Interval: {m.get('interval')} sec, Status: {m.get('status')}\n"

        await message.reply(text)
