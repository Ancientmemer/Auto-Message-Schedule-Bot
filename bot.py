import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from pyrogram import Client

from config.config import BOT_TOKEN, API_ID, API_HASH

from handlers.start import register_start_handler
from handlers.add import register_add_handlers
from handlers.stop import register_stop_handlers
from handlers.status import register_status_handlers
from handlers.broadcast import register_broadcast_handlers


# ================= HTTP SERVER (For UptimeRobot) =================

class PingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"🤖 Auto Message Scheduler Bot is running!")

def run_http_server():
    server = HTTPServer(("0.0.0.0", 10000), PingHandler)
    server.serve_forever()

# Start HTTP server in background thread
threading.Thread(target=run_http_server, daemon=True).start()


# ================= PYROGRAM BOT =================

app = Client(
    "AutoMessageBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register all handlers
register_start_handler(app)
register_add_handlers(app)
register_stop_handlers(app)
register_status_handlers(app)
register_broadcast_handlers(app)

print("🤖 Auto Message Scheduler Bot Started")

app.run()
