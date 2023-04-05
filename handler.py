from aiogram.types import message
import asyncio
from main import bot
from aiogram import types, Dispatcher
from keyboard import keyboard
import json
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)
dictionary = {1: 'Хот-дог',
              2: 'Чебурек',
              3: 'Пицца'}
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id,"тест",reply_markup=keyboard)
    await bot.send_message(chat_id=919865126, text="Вы  получили новый заказ")
    """
    Этот обработчик будет вызываться при получении команды /start
    """
    await message.reply("Привет! Я бот, который может помочь тебе в разных вопросах.")
"""@dp.message_handler(content_type='web_app_data')
async def buy_process(web_app_message):
    await bot.send_invoice(web_app_message.chat.id)"""

@dp.message_handler(content_types="web_app_data") #получаем отправленные данные
async def answer(webAppMes):
   res=json.loads(webAppMes.web_app_data.data)
   print(webAppMes) #вся информация о сообщении
   print(webAppMes.web_app_data.data) #конкретно то что мы передали в бота
   await bot.send_message(webAppMes.chat.id, text=f"получили инофрмацию из веб-приложения: {res}")
   #отправляем сообщение в ответ на отправку данных из веб-приложения
   await bot.send_message(chat_id=919865126, text="Вы  получили новый заказ")
   itogo=0
   for i in range(1,len(res)+1):
       itogo+=int(res[str(i)]['amount'])*res[str(i)]['price']
       await bot.send_message(webAppMes.chat.id, text=f"{res[str(i)]['title']}: {res[str(i)]['amount']}шт {res[str(i)]['price']}руб")
   await bot.send_message(webAppMes.chat.id, text=f"Итого к оплате: {itogo}руб")