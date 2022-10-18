from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp


ikn_button = InlineKeyboardMarkup(row_width=3,
                                inline_keyboad=[
                                 [
                                     InlineKeyboardButton(text="Sms", callback_data='Sms'),
                                     InlineKeyboardButton(text="Tel", callback_data='Tel')
                                ]
                    ])

