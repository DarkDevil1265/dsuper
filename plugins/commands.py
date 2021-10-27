# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .info import get_movie

START_TEXT = """Hello {}
I am a movie information finder bot.

> `I can find information of all movies.`

Made by @malluinstaufollowers"""

JOIN_BUTTONS = [
    InlineKeyboardButton(
        text='📢 Join Channel 📢',
        url='https://t.me/malluinstafollowers'
    )
]

HELP_TEXT = """**Hey, Follow these steps:**

➠ Just send a movie name for information.
➠ I will send the information of movie.

**Available Commands**

/start - Checking Bot Online
/help - For more help
/about - For more about me
/status - For bot status
/settings - For bot settings
/reset - For reset bot settings

Made by @malluinstaufollowers"""

ABOUT_TEXT = """--**About Me 😎**--

🤖 **Name :** [Movie Info Bot](https://telegram.me/{})

👨‍💻 **Developer :** [RJ](https://t.me/malluinstaufollowers)

📢 **Channel :** [RJ](https://t.me/malluinstafollowers)

👥 **Group :** [Mallu Insta Followers](https://t.me/malluinstafollowers)

🌐 **Source :** [👉 Click here](https://github.com/DarkDevil1265/RJ_movies_v2)
📝 **Language :** [Python3](https://python.org)

🧰 **Framework :** [Pyrogram](https://pyrogram.org)

📡 **Server :** [Heroku](https://heroku.com)"""

SETTINGS_TEXT = "**Settings**"

 
RESET_TEXT = "**Are you sure for reset.**"
BUTTONS = InlineKeyboardMarkup(
    [JOIN_BUTTONS]
)

@Client.on_message(filters.private & filters.command(["start"]), group=-1)
async def start(bot, update):
    if update.text == "/start":
        await update.reply_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )
    else:
        movie = update.text.split(" ", 1)[1]
        await get_movie(bot, update, movie)
