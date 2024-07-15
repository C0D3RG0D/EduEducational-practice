from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.fsm.models import NewAd, UpdateAd
from bot.database.method import new_ad, update_ad
import bot.config as config

admin_router = Router()


@admin_router.message(Command('addItem'))
async def add_item_first(message: Message, state: FSMContext):
    if message.from_user.id != config.ADMIN_ID:
        await message.reply(text='У вас не достаточно прав для использования этой команды!')

    else:
        await state.set_state(NewAd.id_ad)
        await message.answer('Введите id объявления')


@admin_router.message(NewAd.id_ad)
async def add_item_second(message: Message, state: FSMContext):
    await state.update_data(id_ad=message.text)
    await state.set_state(NewAd.name)
    await message.answer('Введите название объявления')


@admin_router.message(NewAd.name)
async def add_item_third(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(NewAd.description)
    await message.answer('Введите описание обьявление')


@admin_router.message(NewAd.description)
async def add_item_fourth(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(NewAd.photo)
    await message.answer('Введите айди фотографии к объявлению')


@admin_router.message(NewAd.photo)
async def add_item_fifth(message: Message, state: FSMContext):
    await state.update_data(photo=message.text)
    await state.set_state(NewAd.price)
    await message.answer('Введите цену')


@admin_router.message(NewAd.price)
async def add_item_final(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()

    if await new_ad(id_ad=int(data["id_ad"]),
                    name=data["name"],
                    description=data["description"],
                    photo_id=data["photo"],
                    price=data["price"]):
        await message.answer('Объявление успешно добавлено!')
        await state.clear()

    else:
        await message.answer('Объявление с таким id уже существует!')
        await state.clear()


@admin_router.message(Command('editItem'))
async def edit_item_first(message: Message, state: FSMContext):
    if message.from_user.id != config.ADMIN_ID:
        await message.reply(text='У вас не достаточно прав для использования этой команды!')

    else:
        await state.set_state(UpdateAd.id_ad)
        await message.answer('Введите id объявления, которое хотите изменить/обновить')


@admin_router.message(UpdateAd.id_ad)
async def edit_item_second(message: Message, state: FSMContext):
    await state.update_data(id_ad=message.text)
    await state.set_state(UpdateAd.name)
    await message.answer('Введите новое название объявления(Если его не нужно изменять введите None)')


@admin_router.message(UpdateAd.name)
async def edit_item_third(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UpdateAd.description)
    await message.answer('Введите новое описание объявления(Если его не нужно изменять введите None)')


@admin_router.message(UpdateAd.description)
async def edit_item_fourth(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(UpdateAd.photo)
    await message.answer('Введите новое id фото объявления(Если его не нужно изменять введите None)')


@admin_router.message(UpdateAd.photo)
async def edit_item_fifth(message: Message, state: FSMContext):
    await state.update_data(photo=message.text)
    await state.set_state(UpdateAd.price)
    await message.answer('Введите новую цену товара(Если ее не нужно изменять введите None)')


@admin_router.message(UpdateAd.price)
async def edit_item_final(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()

    if await update_ad(id_ad=data['id_ad'],
                       name=data['name'],
                       description=data['description'],
                       photo_id=data['photo'],
                       price=data['price']):
        await message.answer('Обьявление успешно измененно')
        await state.clear()

    else:
        await message.answer('Объявления с таким id не существует!')
        await state.clear()


@admin_router.message(F.photo)
async def get_photo_id(message: Message):
    if message.from_user.id != config.ADMIN_ID:
        await message.reply(text='У вас не достаточно прав для использования этой команды!')

    else:
        await message.answer(f'ID фото {message.photo[-1].file_id}')
