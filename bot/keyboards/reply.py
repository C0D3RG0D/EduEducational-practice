from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def user_menu():
    keyboard = ReplyKeyboardBuilder()

    keyboard.add(KeyboardButton(text='/start'))
    keyboard.add(KeyboardButton(text='/help'))
    keyboard.add(KeyboardButton(text='/catalog'))

    return keyboard.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите кнопку ниже...')


async def admin_menu():
    keyboard = ReplyKeyboardBuilder()

    keyboard.add(KeyboardButton(text='/start'))
    keyboard.add(KeyboardButton(text='/help'))
    keyboard.add(KeyboardButton(text='/addItem'))
    keyboard.add(KeyboardButton(text='/editItem'))
    keyboard.add(KeyboardButton(text='/catalog'))

    return keyboard.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите кнопку ниже...')
