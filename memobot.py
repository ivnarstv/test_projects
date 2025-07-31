import os
import glob
import telebot
import random
from telebot import types

bot = telebot.TeleBot('7759496911:AAE23cTJAKfWSx6x9vi_bnmJlhEPKrjx6Ns')


image_folder_path = 'mems'

image_files = glob.glob(os.path.join(image_folder_path, '*.jpg'))



@bot.message_handler(commands=["start"])
def start(m):

    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('/mem')
    keyboard.add(button1)

    bot.send_message(m.chat.id, 'Привет! Я бот, который отправляет мемы. Для получения мема используй команду /mem', reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    random_image = random.choice(image_files)
    if message.text == '/mem':
        with open(random_image, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)


bot.polling(none_stop=True, interval=0)
