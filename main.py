import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import common, navigation, guides

async def main():
    logging.basicConfig(level=logging.INFO)

    # Инициализируем бот и диспетчер
    bot = Bot(token='TOKEN')  # Замените на ваш токен
    dp = Dispatcher()

    # Регистрируем роутеры
    dp.include_router(common.router)
    dp.include_router(navigation.router)
    dp.include_router(guides.router)

    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
