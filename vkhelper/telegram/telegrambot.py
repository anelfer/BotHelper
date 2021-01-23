import telebot
import requests
import logging
from telebot.types import InputMediaPhoto, InputMediaVideo

def send_telegram(msg, TELTOKEN, data):
    bot = telebot.TeleBot(token=TELTOKEN)
    attachments_list = []
    print(len(data.attachments))
    for i in range(len(data.attachments)):
        print(data.attachments[i]['type'])
        if data.attachments[i]['type'] == 'photo':
            print('typePh')
            if len(attachments_list) < 1:
                attachments_list.append(InputMediaPhoto(data.attachments[i]["photo"]['sizes'][-1]['url'], msg))
            attachments_list.append(InputMediaPhoto(data.attachments[i]["photo"]['sizes'][-1]['url']))
        if data.attachments[i]['type'] == 'video':
            print("typeVi")
            print(f'https://vk.com/video{data.attachments[i]["video"]["owner_id"]}_{data.attachments[i]["video"]["id"]}')
            if len(attachments_list) < 1:
                attachments_list.append(InputMediaVideo(f'https://vk.com/video{data.attachments[i]["video"]["owner_id"]}_{data.attachments[i]["video"]["id"]}', msg))
            attachments_list.append(InputMediaVideo(f'https://vk.com/video{data.attachments[i]["video"]["owner_id"]}_{data.attachments[i]["video"]["id"]}'))
    logging.info(attachments_list)
    bot.send_media_group("-248326565", attachments_list)
    bot.send_video("-248326565", "https://vk.com/video247155585_456239456")
