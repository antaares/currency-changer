from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def WalletsPage(lang: str):
        back_text = {
            'uz': '🔙 Bosh menyu',
            'ru': '🔙 Главное меню'}
        wallets_page = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=back_text[lang]),
                ],
                [
                    KeyboardButton(text="➕UZCARD / HUMO"),
                    KeyboardButton(text="➕WMZ USD"),
                ],
                [
                    KeyboardButton(text="➕QIWI RUB"),
                    KeyboardButton(text="➕PERFECTMONEY USD"),
                ],
                [
                    KeyboardButton(text="PAYEER USD/RUB"),
                    KeyboardButton(text="USD / TRC20")
                ]
            ],
            resize_keyboard=True
        )
        return wallets_page