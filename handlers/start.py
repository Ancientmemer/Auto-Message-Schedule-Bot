import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PICS = [
    "https://graph.org/file/0b6a4bc9134932e9c348c-011d15ec8b216a2d00.jpg",
    "https://graph.org/file/84013fb867846835a3588-37bd86de61757025a7.jpg",
    "https://graph.org/file/9485b9d55052846909b1d-c960030f5ccc57a716.jpg"
]

def register_start_handler(app):
    @app.on_message(filters.command("start") & filters.private)
    async def start(_, message):
        await message.reply_photo(
            random.choice(PICS),
            caption="🍿 Welcome!\nAuto Message Scheduler Bot",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Community", url="https://t.me/jb_links")],
                [InlineKeyboardButton("Group", url="https://t.me/trixel_movies")]
            ])
        )
