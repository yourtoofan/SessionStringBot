from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/The_Incricible")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/The_incricible")],
    ]

    START = """
Hey {}

Welcome to {}

If you don't trust this bot, 
> Please stop reading this message
> Delete this chat

Still reading?
You can use me to generate pyrogram (even version 2) and telethon string session. Use below buttons to learn more !

By @ELUpdates
    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @zoyu_support

Source Code : [Click Here](https://github.com/LEGEND_MICKEY)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @Legend_mickey
    """
