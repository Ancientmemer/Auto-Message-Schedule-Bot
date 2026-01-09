from pyrogram import filters
from database.mongodb import get_all
from utils.admin_check import is_admin

def register_status_handlers(app):

    @app.on_message(filters.command("status") & (filters.group | filters.supergroup))
    async def status(client, message):

        if not await is_admin(client, message):
            return

        msgs = get_all(message.chat.id)
        if not msgs:
            return await message.reply("❌ No scheduled messages")

        text = "📊 Status List:\n"
        for i, m in enumerate(msgs, 1):
            text += f"{i}. Every {m['interval']} sec | {m['status']}\n"

        await message.reply(text)
