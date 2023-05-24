from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text

import asyncio
from keyboards.default.general_page import GeneralPage


from loader import dp, db

from keyboards.inline.set_language import langs



TEXT =  {
    'start': "Выберите язык интерфейса💬\n\n"\
        "Interfeys tilini tanlang:/Choose language",
    'general': {
        'uz': "MyChangerUzBot - bu O'zbekiston hududidagi ishonchli valyuta almashuv servisi.",
        'ru': "MyChangerUzBot - это надежный сервис обмена валют на территории Узбекистана."
    },
    'entry-name': {
        'uz': "Botdan foydalanishni davom etish uchun iltimos o'z F.I.Sh'ni kiriting\n"\
                "Misol: Rustamov Mustafo Mahmudovich",
        'ru': "Пожалуйста, введите свой Ф.И.Ш, чтобы продолжить использование бота\n"\
                 "Пример: Рустамов Мустафо Махмудович"
    },
    
}



full_name = None

# one time import
from aiogram.dispatcher.filters.state import State,StatesGroup

class EntryName(StatesGroup):
    entry_name = State()








@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    await message.answer(TEXT['start'], reply_markup = langs)
    
    




@dp.callback_query_handler(Text(startswith="set_lang"), state="*")
async def set_lang(call: types.CallbackQuery, state: FSMContext):
    lang = call.data.split("|")[1]
    await call.answer(cache_time=0)
    await call.message.delete()
    # full_name = await db.get_full_name(call.message.chat.id)
    data = await state.get_data()
    full_name = data.get("full_name")
    if full_name is None:
        await call.message.answer(TEXT['entry-name'][lang])
        await state.set_state("entry-name")
        await state.update_data(lang=lang)
        return await EntryName.entry_name.set()
    
    # await db.set_lang(lang, call.message.chat.id)
    await call.message.answer(TEXT['general'][lang], reply_markup= await GeneralPage(lang))
    



@dp.message_handler(state=EntryName.entry_name)
async def entry_name(message: types.Message, state: FSMContext):
    lang = (await state.get_data()).get("lang")
    full_name = message.text
    await state.update_data(full_name=full_name)
    await state.finish()
    await message.answer(TEXT['general'][lang], reply_markup = await GeneralPage(lang))