from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default import menuPython
from keyboards.default.mainKeyboard import menu
from keyboards.default.courseKeyboard import menuCourses
from keyboards.default import *


from loader import dp

@dp.message_handler(text=["Bosh menyu", "Boshiga"])
@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu)

@dp.message_handler(text="📋 Telegram bot")
async def send_link(message: types.Message):
    await message.answer("Mukammal Telegram bot kursi: https://mohirdev.uz/courses/telegram")

@dp.message_handler(text="📝 Kurslar")
async def show_courses(message: types.Message):
    await message.answer("Kurslarni tanlang", reply_markup=menuCourses)
    
    

@dp.message_handler(text="Pyhon basics")
async def show_course(message: types.Message):
    await message.answer("python kurslari", reply_markup=menuPython.menu_python)

