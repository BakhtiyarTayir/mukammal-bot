from re import A
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startMenuKeyboard import menuStart
from keyboards.inline.productsKeyboard import categoryMenu, courseMenu


from loader import dp

@dp.message_handler(text_contains="Mahsulotlar")
async def menu_products(message: types.Message):
    await message.answer("Mahsulotlar", reply_markup=categoryMenu)

@dp.callback_query_handler(text="courses")
async def buy_courses(call: types.CallbackQuery):
    await call.message.answer("Kurslar", reply_markup=courseMenu)
    await call.answer(cache_time=60)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Salom", reply_markup=menuStart)
