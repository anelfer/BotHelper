import telebot
from telebot.types import InputMediaPhoto, InputMediaVideo
import os
from dotenv import load_dotenv
import json

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

print("Bot Started")
bot = telebot.TeleBot(TOKEN, threaded=False)

def send_telegram(msg):
    bot.send_message("-248326565", msg)
    return True

@bot.message_handler(commands=['get_id'])
def get_idChat(message):
    bot.send_message("545249849", message.chat.id)


@bot.message_handler(commands=['send_photo'])
def send_photo(message):
    # print(list_img)
    # print(json.dumps(list_img))
    bot.send_media_group("-248326565",
                         [
                            InputMediaPhoto('https://static.integromat.com/img/templates/1454.png', "TestMessage"),
                            InputMediaPhoto('https://i.stack.imgur.com/31W38.png')
                         ])

# @bot.message_handler(content_types=["text"])
# def resend(message):
#     bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling()
