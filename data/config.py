from environs import Env

# environs kutubxonasidan foydalanish


env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5694405512:AAHIC81AG6I8o3xJSNlQB2bFuWyEqxJd1TI"  # Bot toekn
ADMINS = [1459481069]  # adminlar ro'yxati




# @dp.callback_query_handler()
# async def callabeck_query(call):
#     if call.data == 'btn_1':
#         print("OK")


# IP = env.str("ip")  # Xosting ip manzili
