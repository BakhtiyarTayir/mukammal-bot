from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_python = ReplyKeyboardMarkup( [
    [
        KeyboardButton('#00 Kirish'),
        KeyboardButton('#01 Kerakli dasturlar'),
        KeyboardButton('#02  Hello world!'),
    ], 
    [
        KeyboardButton('#03 Ortga'),
        KeyboardButton('Boshiga'),
    ], 
], resize_keyboard=True)