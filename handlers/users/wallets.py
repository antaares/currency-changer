from keyboards.default.wallets_page import WalletsPage
from loader import dp, db

from aiogram import types


from aiogram.dispatcher.filters.builtin import Text



TEXT = {
    'main': {
        'uz': "Sizni hamyonlaringiz",
        'ru': "Ваши кошельки"
},
}    




@dp.message_handler(Text(equals="💳 Hamyonlar"), state="*")
async def wallets_page(message: types.Message):
    # lang = await db.get_lang(message.chat.id)
    lang = "uz"
    await message.answer(TEXT['main'][lang], reply_markup= await WalletsPage(lang))