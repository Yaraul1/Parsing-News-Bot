from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Здравствуйте, я показыаю новости с сайта 4pda!')


