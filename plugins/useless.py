from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private & filters.incoming)
async def useless(_, message):
    if USER_REPLY_TEXT in message.text:
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Visit Website", url="https://example.com")]
            ]
        )
        await message.reply_text(USER_REPLY_TEXT, reply_markup=keyboard)

'''
USER_REPLY_TEXT = "❌ Don't send me messages directly I'm only File Share bot!"
URL_BUTTON_TEXT = "Visit Website"
URL_BUTTON_URL = "https://example.com"

@Bot.on(events.NewMessage)
async def handle_message(event):
    message = event.message
    if message.is_private and USER_REPLY_TEXT in message.text:
        # Create an inline keyboard with a URL button
        button = types.BotInlineKeyboardButton(text=URL_BUTTON_TEXT, url=URL_BUTTON_URL)
        keyboard = types.InlineKeyboardMarkup([[button]])
        
        # Reply to the user with the predefined message and the URL button
        await message.reply(USER_REPLY_TEXT, buttons=keyboard)
'''
