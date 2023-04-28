"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import random

markup = ReplyKeyboardMarkup()
markup.add('/start')
# photo = open(r'/home/artem/Desktop/Images/05304c9e8d8b327db682d23cde2244b3.jpg', 'rb')

API_TOKEN = '6151736053:AAEW2UGGVd4MNJ4msO1dnJYALt6GOmFKiwo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

catigories = ['Sport', 'Creation', 'Cooking', 'Add exercise']
exercises_sport = ['Do 50 squats','Do 50 pushups','Do 50 pull ups']
exercises_creation = ['Write a letter to a friend','Read a book', 'Write python code']
exercises_cooking = ['Cook dinner', 'Bake bread', 'Cook soup']

text = 'Select a category'
text_2 = 'Enter task'

messagemarkup = types.ReplyKeyboardMarkup()
button_1 =types.InlineKeyboardButton('Sport', catigories[0])
button_2 = types.InlineKeyboardButton('Creation', catigories[1])
button_3 = types.InlineKeyboardButton('Cooking', catigories[2])
button_4 = types.InlineKeyboardButton('Add exercise', catigories[3])
messagemarkup.add(button_1, button_2, button_3, button_4)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # await message.reply(photo)
    await message.reply("Hi!\nI'm Exercisebot!\n")
    await message.reply("Select a category", reply_markup = messagemarkup)
 

@dp.message_handler()
async def echo(message: types.Message):
    sport = random.choice(exercises_sport)
    creation = random.choice(exercises_creation)
    cooking = random.choice(exercises_cooking)
    if str(message.text) == catigories[0]:
        await message.answer(sport)
    elif str(message.text) == catigories[1]:
        await message.answer(creation)
    elif str(message.text) == catigories[2]:
        await message.answer(cooking)

            
        
           
       
            



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)