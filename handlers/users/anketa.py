from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData


@dp.message_handler(Command("form"))
async def send_form(message: types.Message, state: FSMContext):
    await message.answer("To'liq ismingizni kiriting:")
    await PersonalData.fullName.set()

@dp.message_handler(state=PersonalData.fullName)
async def enter_full_name(message: types.Message, state: FSMContext):
    fullName = message.text
    await state.update_data(
        {'name': fullName}
    )
    await message.answer(f"Emailni kiriting:")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.email)
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(
        {'email': email}
    )

    await message.answer(f"Telefon raqamingizni kiriting:")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.phoneNum)
async def enter_phone_num(message: types.Message, state: FSMContext):
    phoneNum = message.text
    await state.update_data(
        {'phone': phoneNum}
    )

    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msg = "Quyidagi ma'lumotlar qabul qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Email - {email}\n"
    msg += f"Telefon raqami - {phone}"
    await message.answer(msg)

    await state.finish()
