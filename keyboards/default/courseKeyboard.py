from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuCourses = ReplyKeyboardMarkup( [
    [
        KeyboardButton('Pyhon basics'),
        KeyboardButton('Django'),

    ], 
    [
        KeyboardButton('Bosh menyu'),
    ]
], resize_keyboard=True)