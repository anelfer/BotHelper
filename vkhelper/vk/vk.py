import vk_api
import requests
import json
import os
import asyncio
import logging
from vk_api.bot_longpoll import *
from dotenv import load_dotenv
from vkhelper.telegram.telegram import send_telegram
from vkhelper.discord.discordBot import send_discord
from vkhelper.vk.func import *

helper = VkFunc()
logger = logging.getLogger(__name__)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:

        response = event.obj.message['text'].lower()
        chat_id = int(event.obj.message['peer_id']) - 2000000000
        peer_id = event.obj.message['peer_id']

        logger.info(event.obj.message) #Logging everyone message

        helper.forward_to(event.obj.message['text'])
        helper.kick_user()

        if event.from_user or event.from_chat and not event.from_group:
            if response.startswith('test'):
                helper.send_given_msg()
            if response.startswith('бот пидор'):
                vk.method('messages.send',
                          {
                              'peer_id': peer_id,
                              "attachment": 'photo539601753_457239055',
                              'random_id': 0
                          })
            if response.startswith("бот хелп"):
                vk.method('messages.send', {
                    'peer_id': peer_id,
                    'message': 'Я могу: \n '
                               '1) Изменять название беседы с помощью команды: \nбот нейм \nназвание  \n '
                               '2) Изменять аватарку беседы с помощью команды: \n бот фото \n и прикрепленная фотография',
                    'random_id': 0
                })

        if event.from_user or event.from_chat and helper.check_is_admin():
            if response.startswith('бот нейм') and event.from_chat:
                try:
                    if helper.check_second_line(response):
                        helper.chat_name_change(chat_id, helper.check_second_line(response))
                    else:
                        helper.send_given_msg('Вы не ввели название')
                except Exception as e:
                    helper.execption_msg_send(e)
            if response.startswith('бот фото') and event.from_chat:
                try:
                    url = event.message.attachments[0]['photo']['sizes'][-1]['url']
                    r = requests.get(url, allow_redirects=True)
                    open('../../cache/avatars.jpg', 'wb').write(r.content)

                    res = vk.method('photos.getChatUploadServer', {
                        'chat_id': chat_id,
                    })
                    photo_res = requests.post(res['upload_url'], files={'file': open('../../cache/avatars.jpg', 'rb')}).json()

                    vk.method('messages.setChatPhoto', {
                        'file': photo_res['response'],
                    })
                except Exception as e:
                    helper.execption_msg_send(e)
            if response.startswith('бот кик') and event.from_chat:
                try:
                    if "from_id" in event.obj.message['fwd_messages'][0]:
                        member_id = event.obj.message['fwd_messages'][0]['from_id']
                    elif "from_id" in event.obj.message['reply_message']:
                        member_id = event.obj.message['reply_message']['from_id']
                        print(event.obj.message['reply_message']['from_id'])
                    else:
                        member_id = None

                    if member_id != None and member_id != event.obj.message['from_id'] and check_is_admin():
                        vk.method('messages.removeChatUser', {
                            'chat_id': chat_id,
                            'member_id': member_id
                        })
                    else:
                        helper.send_given_msg('Вы не можете себя кикнуть')
                except Exception as e:
                    helper.execption_msg_send('Произошла ошибка, возможно пользователь является администратором или вы его не указали.')