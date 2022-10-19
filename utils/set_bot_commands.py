from aiogram import types
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


async def set_default_commands(dp):

    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish", ),
            types.BotCommand("help", "Yordam"),
        ]
    )


# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):

    # await message.answer("Admin bo'lsangiz quydagilardan birni tanlang!!", reply_markup=btn)
