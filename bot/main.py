import asyncio
from aiogram import Bot, Dispatcher
from handlers.admin import main as admin_main_handlers
from handlers.user import main as user_main_handlers
from config import Config

#функция конфигурирования и запуска бота
async def main():

    #загружаем конфиг в переменную Config
    config: Config = Config()

    #регистрируем бота и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    #регистрируем роутеры в диспетчер
    dp.include_router(admin_main_handlers.router)
    dp.include_router(user_main_handlers.router)

    #пропускаем накопившиемя апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())

