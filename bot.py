from pyrogram import Client, filters, idle
import asyncio
import os

app = Client(
    "test",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

@app.on_message(filters.text)
async def echo(_, msg):
    await msg.reply("✅ I am alive")

async def main():
    await app.start()
    print("BOT STARTED")
    await idle()

asyncio.run(main())
