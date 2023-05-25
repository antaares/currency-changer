from keyboards.default.wallets_page import WalletsPage
from loader import dp, db

from aiogram import types


from aiogram.dispatcher.filters.builtin import Text



TEXT = {
    'main': {
        'uz': "Sizni hamyonlaringiz",
        'ru': "Ваши кошельки"
        },
    'enter_number': {
        'uz': "{wallet_name} hamyon raqamini kiriting",
        'ru': "Введите номер кошелька"
        },
    'wrong_number': {
        'uz': "Siz noto'g'ri raqam kiritdingiz, qayta kiriting:",
        'ru': "Вы ввели неправильный номер, введите еще раз:"
        },
    'finish_entry': {
        'uz': "Sizning hamyon raqamingiz saqlandi.",
        'ru': "Ваш номер кошелька сохранен."
    }    
}



# on etime state
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class EntryWallet(StatesGroup):
    choose_wallet = State()
    enter_number = State()









@dp.message_handler(Text(equals="💳 Hamyonlar"), state="*")
async def wallets_page(message: types.Message):
    # lang = await db.get_lang(message.chat.id)
    lang = "uz"
    await message.answer(TEXT['main'][lang], reply_markup= await WalletsPage(lang))
    await EntryWallet.choose_wallet.set()




@dp.message_handler(state=EntryWallet.choose_wallet)
async def choose_wallet(message: types.Message, state: FSMContext):
    lang = 'uz' #await db.get_lang(call.message.chat.id)
    await message.answer(TEXT['enter_number'][lang].format(wallet_name=message.text), reply_markup= await WalletsPage(lang))
    await EntryWallet.enter_number.set()




@dp.message_handler(state=EntryWallet.enter_number)
async def enter_number(message: types.Message, state: FSMContext):

    lang = 'uz'

    is_valid = True # await check_wallet(message.text)
    if is_valid is False:
        await message.answer(TEXT['wrong_number'][lang], reply_markup= await WalletsPage(lang))
        return await EntryWallet.enter_number.set()
    await message.answer(TEXT['finish_entry'][lang])
    await message.answer(TEXT['main'][lang], reply_markup= await WalletsPage(lang))