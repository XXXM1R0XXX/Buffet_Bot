import logging
from config import BOT_TOKEN
from aiogram import Bot, executor
from handler import *
from aiogram.utils.web_app import safe_parse_webapp_init_data
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

# Устанавливаем уровень логов на INFO, чтобы видеть сообщения об ошибках
logging.basicConfig(level=logging.INFO)

# Создаем бота
bot = Bot(token=BOT_TOKEN)


if __name__ == '__main__':
    # Запускаем цикл обработки входящих сообщений
    executor.start_polling(dp, skip_updates=True)