from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import telebot

from data import config


# bot = telebot.TeleBot('5694405512:AAHIC81AG6I8o3xJSNlQB2bFuWyEqxJd1TI')

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
