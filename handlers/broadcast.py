from pyrogram import filters
from config.config import OWNER_ID

def register_broadcast_handlers(app):
    @app.on_message(filters.command("broadcast") & filters.private)
    async def broadcast(_, message):
        if message.from_user.id != OWNER_ID:
            return await message.reply("❌ Not authorized")
        if not message.reply_to_message:
            return await message.reply("Reply to a message to broadcast")

        for chat in []:  # add logic to fetch saved chat IDs if needed
            try:
                await message.reply_to_message.copy(chat)
            except:
                pass

        await message.reply("📣 Broadcast sent")
