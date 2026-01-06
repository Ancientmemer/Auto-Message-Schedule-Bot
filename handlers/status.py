from pyrogram import filters
from database.mongodb import get_all
from utils.admin_check import is_admin

def register_status_handlers(app):
    @app.on_message(filters.command("status") & filters.group)
    async def status(_, message):
        if not await is_admin(_, message):
            return
        data = get_all(message.chat.id)
        if not data:
            return await message.reply("No messages")
        text = "📊 Status\n"
        for i, m in enumerate(data, 1):
            text += f"{i}. {m.get('status')}\n"
        await message.reply(text)
