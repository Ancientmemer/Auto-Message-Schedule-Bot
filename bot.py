from pyrogram import Client
from config.config import BOT_TOKEN
from handlers.start import register_start_handler
from handlers.add import register_add_handlers
from handlers.stop import register_stop_handlers
from handlers.status import register_status_handlers
from handlers.broadcast import register_broadcast_handlers

app = Client("AutoMessageBot", bot_token=BOT_TOKEN)

register_start_handler(app)
register_add_handlers(app)
register_stop_handlers(app)
register_status_handlers(app)
register_broadcast_handlers(app)

app.run()
