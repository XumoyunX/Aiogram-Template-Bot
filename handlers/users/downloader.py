import os

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot
from tiktok import tk
from instagram import instadownloader
# from instagram import ins
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery
from pytube import YouTube
# import telebot;


from.youtube_data import ikn_button



@dp.message_handler(Text(startswith='https://www.tiktok.com'))
async def test(message:types.Message):
    natija = tk(message.text)
    qushiq = natija['music']
    btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Musiqasini yuklab olish", url="{}".format(qushiq))]
        ]
    )

    await message.answer_audio(natija['video'], reply_markup=btn)

# @dp.callback_query_handler(Text(startswith='🎵'))
# async  def test2(call: CallbackQuery):
#     await  call.answer(cache_time=60)
#     data = call.data[1:]
#     await call.message.answer_audio(data)



@dp.message_handler(Text(startswith='https://www.instagram.com'))
async def send_media(message:types.Message):
    link1 = message.text
    data = instadownloader(link1=link1)
    if data == "Error":
        await message.answer('Bu URL manzil orqali hech narsa topolmadik!!')
    else:
        if data['type'] == 'image':
            await message.answer_photo(photo=data['media'])
        elif data['type'] == 'video':
            await message.answer_video(video=data['media'])
        elif data['type'] == 'carousel':
            for i in data['media']:
                await message.answer_document(document=i)
        else:

            await message.answer('Bu URL manzil orqali hech narsa topolmadik!!')









@dp.message_handler()
async def test_mesage(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' or 'https"//www.youtube.com/':
        await bot.send_message(chat_id, f"Kutib tuting* : *{yt.title}*\n"
                                        f"*Kanal *: [{yt.author}]({yt.channel_url})")
        await download_youtube_video(url, message, bot)



async def download_youtube_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", "rb") as video:
        btn = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Musiqasini yuklab olish", callback_data = "btn_1")]
        ])
        await bot.send_video(message.chat.id, video, caption="* Video *", reply_markup=btn)
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")


@dp.message_handler(Text(startswith="http"))
async def get_audio(message:types.Message):
    print("pkkk")
    link = message.text
    from io import BytesIO
    buffer=BytesIO()
    url=YouTube(link)
    if url.check_availability() is None:
        audio=url.streams.get_audio_only()
        audio.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        filname=url.title
        await message.answer_audio(audio=buffer, caption=filname)
    else:
        await message.answer("Error")
        print("ok")




@dp.callback_query_handler()
async def callabeck_query(call):
    if call.data == 'btn_1':
        pass 




