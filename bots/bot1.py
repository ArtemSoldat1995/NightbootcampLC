import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5974683133:AAHPgd1B4vw3qPoBmdgiFNaSjzieUWbj41k'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello!\nI'm WeatherBot!\nenter temperature.")



@dp.message_handler()
async def echo(message: types.Message):
    if int(message.text) <= int(0):
        await message.answer('Наденьте куртку, шапку и подштаники!')
    elif int(message.text) < int(10):
        await message.answer('Стоит одеться потеплее!')
    elif int(message.text) >= int(10) and int(message.text) < int(15):
        await message.answer('Нужно одеть ветровку!')
    elif int(message.text) >= int(15) and int(message.text) < int(22):
        await message.answer('Можно одеться легко!') 


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
