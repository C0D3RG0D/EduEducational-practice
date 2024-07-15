from bot.database.models import async_session
from bot.database.models import Item

from sqlalchemy import select, update


async def new_ad(id_ad: int, name: str, description: str, photo_id: str, price: int) -> bool:
    async with async_session() as session:
        item = await session.scalar(select(Item).where(Item.id == id_ad))

        if not item:
            session.add(Item(id=id_ad,
                             name=name,
                             description=description,
                             photo=photo_id,
                             price=price))
            await session.commit()

            return True

        else:
            return False


async def update_ad(id_ad: int, name: str, description: str, photo_id: str, price: int) -> bool:
    async with async_session() as session:
        item = await session.scalar(select(Item).where(Item.id == id_ad))

        if not item:
            return False

        await session.execute(update(Item)
                              .values(name=name,
                                      description=description,
                                      photo=photo_id,
                                      price=price)
                              .where(Item.id == id_ad))
        await session.commit()

        return True


async def select_data():
    async with async_session() as session:
        datas = await session.scalars(select(Item))
        items = datas.fetchall()
        
        return items
    