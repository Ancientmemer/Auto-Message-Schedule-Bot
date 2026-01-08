import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PICS = [
    "https://graph.org/file/0b6a4bc9134932e9c348c-011d15ec8b216a2d00.jpg",
    "https://graph.org/file/84013fb867846835a3588-37bd86de61757025a7.jpg",
    "https://graph.org/file/9485b9d55052846909b1d-c960030f5ccc57a716.jpg"
]

START_TEXT = """
👋 Welcome to Auto Time Scheduler Bot! 🤖⏰

This bot helps you schedule messages automatically and send them at the perfect time ⏳

✨ Features:
📨 Schedule messages for future time  
🔁 Auto repeat messages  
⏰ Save time with smart scheduling  
⚡ Simple, fast & reliable  

🚀 Use /add in a group to schedule messages!
"""

def register_start_handler(app):

    @app.on_message(filters.command("start"))
    async def start(_, message):
        await message.reply_photo(
            random.choice(PICS),
            caption=START_TEXT,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🌐 Community", url="https://t.me/jb_links")],
                [InlineKeyboardButton("👥 Group", url="https://t.me/trixel_movies")]
            ])
        )
