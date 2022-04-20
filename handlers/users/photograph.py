from aiogram import types
from pathlib import Path

from loader import dp
from utils import photo_link
from utils import remove_background

download_path = Path().joinpath("downloads","images")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]
    link = await photo_link(photo)
    # await msg.answer(link)
    image = await remove_background(link)
    await msg.reply_document(document=image, caption="Background removed")

