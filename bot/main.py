import asyncio
from aiogram import Bot, Dispatcher
from handlers.admin import main as admin_main
from handlers.user import main as user_main
from config import Config
#функция конфигурирования и запуска бота
async def main():

    #загружаем