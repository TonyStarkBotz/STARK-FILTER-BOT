# Don't Remove Credit @TonyStark_Botz
# Join our Telegram Channel For Amazing Bot @TonyStark_Botz
# Ask Doubt on telegram @TonyStarkBotzXSupport

from aiohttp import web
from .route import routes

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
