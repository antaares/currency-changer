from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



langs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="set_lang|uz"),
            InlineKeyboardButton(text="🇷🇺 Русский язык", callback_data="set_lang|ru"),
        ]
    ]
        )
