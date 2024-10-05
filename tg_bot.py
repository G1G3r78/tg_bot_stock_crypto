import asyncio

from aiogram import Bot, Dispatcher

from handlers import router

from constants import API


async def main():
    bot = Bot(token=API)
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("exit")