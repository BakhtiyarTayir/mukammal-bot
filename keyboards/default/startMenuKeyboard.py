from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📚 Mahsulotlar"),
            KeyboardButton(text="📝 Qo'llanma"),
        ],
    ],
    resize_keyboard=True)