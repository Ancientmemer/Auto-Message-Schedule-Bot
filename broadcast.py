from pyrogram import filters
from config.config import OWNER_ID

def register_broadcast_handlers(app):
    @app.on_message(filters.command("broadcast") & filters.private)
    async def broadcast(_, message):
        if message.from_user.id != OWNER_ID:
            return
        await message.reply("Broadcast placeholder")
