# Don't Remove Credit @TonyStark_Botz
# Join our Telegram Channel For Amazing Bot @TonyStark_Botz
# Ask Doubt on telegram @TonyStarkBotzXSupport

from pyrogram import Client, filters
from plugins.Extra.engine import ask_ai


@Client.on_message(filters.command('openai'))
async def openai_ask(client, message):
    if len(message.command) == 1:
       return await message.reply_text("Give an input!")
    m = await message.reply_text("👀")
    await ask_ai(client, m, message)
