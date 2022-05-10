from aiogram.dispatcher.filters.state import State, StatesGroup


class PersonalData(StatesGroup):
    fullName = State()
    email = State()
    phoneNum = State()