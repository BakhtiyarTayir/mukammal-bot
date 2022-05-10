from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup( [
    [
        KeyboardButton(text="contact", request_contact=True),
        KeyboardButton(text="location", request_location=True),
    ],
], resize_keyboard=True)