from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startKeyboard import start_menu

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")

# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer("telefon raqamingizni yuboring", reply_markup=start_menu)
