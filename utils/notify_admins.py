import logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters import Text

b1 = KeyboardButton("👥 User son 👥")
b2 = KeyboardButton("Post")

kb_clinet = ReplyKeyboardMarkup(resize_keyboard=True)
kb_clinet.add(b1).add(b2)



# keyboard = InlineKeyboardMarkup()
# menu_1 = InlineKeyboardButton(text='Расписание 🗓', callback_data="take")
# menu_2 = InlineKeyboardButton(text='Программы 💾', callback_data="menu_2")
# menu_3 = InlineKeyboardButton(text='О проекте  📌', callback_data="menu_3")
# keyboard.add(menu_1, menu_2, menu_3)
# @dp.callback_query_handler()
async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:

        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi\nPost jo'nata olasiz  va User soni ko'ra olasiz", reply_markup=kb_clinet)

        except Exception as err:
            logging.exception(err)


@dp.message_handler()
async def menu1(message: types.Message):
    if message.text == "👥 User son 👥":
        with open('start', 'r') as f:
            g = 0
            for i in f:
                g += 1
            await message.answer(f"👤ADMIN👤:\n\n👥Start bosgan User soni: {g} ✅\n\n\n")
    elif message.text == "Post":
        print("ok ")
        await message.answer("Bunaqa Malumot yuq")

# @dp.callback_query_handler(lambda call: call.data == 'take' )
# async def agree_ref_start(query: types.CallbackQuery):
#     if query.data == 'take':
#         print('ok')
