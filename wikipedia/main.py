import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
from config import token

wikipedia.set_lang('uz')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_message(message: types.Message):
    await message.reply(f'Assalomu alaykum {message.from_user.last_name}, Wikipedia botiga xush kelipsiz!\n Matn kiriting:')


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)