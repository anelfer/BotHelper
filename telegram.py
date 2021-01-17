import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

def send_telegram(msg):
    bot = telebot.TeleBot(TOKEN)
    bot.send_message("-1001291115084", msg)
    return True

if __name__ == '__main__':
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['get_id'])
    def get_idChat(message):
        bot.send_message("545249849", message.chat.id)


    # @bot.message_handler(content_types=["text"])
    # def resend(message):
    #     bot.send_message(message.chat.id, message.text)
    bot.polling()
    print("Bot Started")