import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "8374306367:AAE--fw5XDpVM4lELOm5rgx5ALeeaLUDQDQ"  # @BotFather берган токенни қўйинг

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Янги одам кирса хабарни ўчиради
@dp.message_handler(content_types=["new_chat_members"])
async def on_user_join(message: types.Message):
    try:
        await message.delete()
    except:
        pass

# Одам чиқса хабарни ўчиради
@dp.message_handler(content_types=["left_chat_member"])
async def on_user_leave(message: types.Message):
    try:
        await message.delete()
    except:
        pass

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
