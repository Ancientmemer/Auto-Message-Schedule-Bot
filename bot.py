import asyncio
from pyrogram import Client, idle, filters
from config.config import BOT_TOKEN, API_ID, API_HASH

app = Client(
    "AutoMessageBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.text)
async def echo(client, message):
    print("MESSAGE RECEIVED")
    await message.reply("👀 I am alive")

async def main():
    await app.start()
    print("🤖 Bot started")
    await idle()

if __name__ == "__main__":
    asyncio.run(main())
