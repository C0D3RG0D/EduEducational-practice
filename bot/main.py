from aiogram import Bot, Dispatcher

from bot.misc import TgKeys
from bot.handlers import user_router, admin_router
from bot.database import init_models


def register_all_routers(dp: Dispatcher):
    dp.include_routers(admin_router, user_router)


async def start_bot():
    await init_models()
    bot = Bot(token=TgKeys.TOKEN)
    dp = Dispatcher()

    register_all_routers(dp)

    await dp.start_polling(bot)
