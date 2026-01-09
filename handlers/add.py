from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.admin_check import is_admin
from database.mongodb import add_message

TIMES = {
    "30s": 30, "1m": 60, "5m": 300,
    "10m": 600, "20m": 1200, "30m": 1800,
    "1h": 3600, "2h": 7200, "5h": 18000
}

def register_add_handlers(app):

    @app.on_message(filters.command("add") & filters.group)
    async def add(client, message):

        if not await is_admin(client, message):
            return

        if not message.reply_to_message:
            return await message.reply("❗ Reply to a message first")

        buttons = [
            [InlineKeyboardButton(
                k,
                callback_data=f"set_{v}_{message.reply_to_message.id}"
            )]
            for k, v in TIMES.items()
        ]

        await message.reply(
            "⏱ Select time",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    @app.on_callback_query(filters.regex("^set_"))
    async def set_time(client, cq):

        _, interval, msg_id = cq.data.split("_")
        interval = int(interval)
        msg_id = int(msg_id)

        chat_id = cq.message.chat.id
        original = await client.get_messages(chat_id, msg_id)

        add_message({
            "chat_id": chat_id,
            "text": original.text or original.caption,
            "interval": interval,
            "status": "running",
            "last_sent": 0
        })

        await cq.answer("Scheduled!", show_alert=True)
        await cq.message.edit("✅ Auto message scheduled!")
