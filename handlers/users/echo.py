from aiogram import types

from loader import dp
from utils.notify_admins import kb_clinet


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    # pass
    if message.text == "User son":
        with open('start', 'r') as f:
            await message.answer(f.read())
    else:
        await message.answer("Bunaqa Malumot yuq")

