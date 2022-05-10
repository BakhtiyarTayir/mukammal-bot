from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup( [
    [
        KeyboardButton('📋 Telegram bot'),
        KeyboardButton('📝 Kurslar'),
    ],  
], resize_keyboard=True)