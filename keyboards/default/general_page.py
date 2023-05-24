from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



async def GeneralPage(language: str):
    if language == 'uz':
        general_page = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="🔄Valyuta ayirboshlash"),
                ],
                [
                    KeyboardButton(text="💳 Hamyonlar"),
                    KeyboardButton(text="📊Kurs | 💰Zahira"),
                ],
                [
                    KeyboardButton(text="♻️ Almashuvlar"),
                    KeyboardButton(text="⚙️ Sozlamalar"),
                ],
                [
                    KeyboardButton(text="👥Referal | 💵Bonus"),
                    KeyboardButton(text="📞Aloqa | 🛡Yordam")
                ]
            ],
            resize_keyboard=True
        )
    elif language == 'ru':
        general_page = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="💳 Кошельки"),
                    KeyboardButton(text="📊Курс | 💰Резервы"),
                ],
                [
                    KeyboardButton(text="♻️ История заявок"),
                    KeyboardButton(text="⚙️ Настройки"),
                ],
                [
                    KeyboardButton(text="👥 Реферал | 💵 Бонус"),
                    KeyboardButton(text="📞Контакты | 🛡Помощь")
                ]
            ],
            resize_keyboard=True
        )
    return general_page