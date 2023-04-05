from aiogram import *
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

web_app=WebAppInfo(url='https://new212.ru/client/buyer/goods/index.html')
keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Site",web_app=web_app)]
    ],
    resize_keyboard=True
)
cb=CallbackData('btn','action')
key=InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton('Pay',collback_data='btn:buy')]]
)