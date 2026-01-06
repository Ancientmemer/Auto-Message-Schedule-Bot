import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PICS = [
    "https://graph.org/file/1a6821fcdc7fd4aae1eeb.jpg",
    "https://graph.org/file/6040b38cb51f5dcea0495.jpg",
    "https://graph.org/file/2a5b38cb51f5dcea0495.jpg"
]

def register_start_handler(app):
    @app.on_message(filters.command("start") & filters.private)
    async def start(_, message):
        await message.reply_photo(
            random.choice(PICS),
            caption="🍿 Welcome! Auto Message Scheduler Bot",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Community", url="https://t.me/yourcommunity")],
                [InlineKeyboardButton("Group", url="https://t.me/yourgroup")]
            ])
        )
