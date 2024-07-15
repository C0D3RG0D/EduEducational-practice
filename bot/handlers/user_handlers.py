from aiogram import Router
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram.filters import CommandStart, Command

from bot.keyboards import user_menu, admin_menu
from bot.database.method import select_data
from bot.misc import TgKeys
import bot.config as config

user_router = Router()


@user_router.message(CommandStart())
async def start(message: Message):
    if message.from_user.id == config.ADMIN_ID:
        await message.reply(text='Приветствую вас, Администратор!', reply_markup=await admin_menu())

    else:
        await message.answer(config.start_message.format(message.from_user.first_name,
                                                         message.from_user.last_name,
                                                         message.from_user.id),
                             reply_markup=await user_menu())


@user_router.message(Command('help'))
async def helps(message: Message):
    await message.answer(config.help_message)


@user_router.message(Command('terms'))
async def terms(message: Message):
    await message.answer(config.development_message)


@user_router.message(Command('catalog'))
async def catalog(message: Message):
    data = await select_data()

    if TgKeys.PAYMENT_TOKEN.split(':')[1] == 'TEST':
        await message.answer('''Работает тестовая платежная система\nЧтобы расплатиться используйте этои данные\n 
        Номер карты: 6390 0200 0000 000003\nДата действия/истечение: 2024/12\nCVC: 123\nПроверочный код: 12345678''')

    for i in data:
        await message.answer_invoice(title=i.name,
                                     description=i.description,
                                     provider_token=TgKeys.PAYMENT_TOKEN,
                                     currency='rub',
                                     photo_url=i.photo,
                                     photo_height=520,
                                     photo_width=520,
                                     photo_size=520,
                                     is_flexible=False,
                                     prices=[LabeledPrice(label=i.name, amount=i.price * 100)],
                                     start_parameter='time-machine-example',
                                     payload='time-machine-payload')


@user_router.pre_checkout_query(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)


@user_router.message()
async def echo(message: Message):
    await message.answer(message.text)
