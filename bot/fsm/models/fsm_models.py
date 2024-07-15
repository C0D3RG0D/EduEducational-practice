from aiogram.fsm.state import StatesGroup, State


class NewAd(StatesGroup):
    id_ad = State()
    name = State()
    description = State()
    photo = State()
    price = State()


class UpdateAd(StatesGroup):
    id_ad = State()
    name = State()
    description = State()
    photo = State()
    price = State()

