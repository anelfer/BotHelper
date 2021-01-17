from vk_api.bot_longpoll import *
from vk_api import exceptions
import vk_api
import time
import requests
import json
import os
from dotenv import load_dotenv
from telegram import send_telegram
from discordBot import send_discord
import asyncio

load_dotenv()
TOKEN = os.getenv('VK_TOKEN')

# Connect
vk = vk_api.VkApi(token=TOKEN)
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, 182910634)

print('VKbotStart')

def ChatNameChange(chat_id, name):
    try:
        vk.method('messages.editChat', {
            'chat_id': chat_id,
            'title': name
        })
        vk.method('messages.send', {
            'peer_id': event.obj.message['peer_id'],
            'message': 'Название успешно изменено',
            'random_id': 0
        })
    except Exception as e:
        ExecptionMsgSend(e)

def ExecptionMsgSend(e):
    vk.method('messages.send', {
        'peer_id': event.obj.message['peer_id'],
        'message': e,
        'random_id': 0
    })

def SendTestMSG(message = 'Тестовое cообщение'):
    vk.method('messages.send', {
        'peer_id': peer_id,
        'message': message,
        'random_id': 0
    })

def CheckSecondLine(response):
    if response.find('\n') != -1:
        return response[response.find('\n')::]
    return False

def CheckIsAdmin():
    check = vk.method('messages.getConversationMembers', {
        'peer_id': peer_id,
    })
    for i in check['items']:
        if i['member_id'] == event.obj.message['from_id']:
            admin = i.get('is_admin', False)
            if admin == True:
                return True
    return False

def KickUser():
    try:
        if event.obj.message['action']['type'] == 'chat_kick_user':
            keyboard = {

                "inline": True,
                "buttons": [
                    [{
                        "action": {
                            "type": "text",
                            "payload": '{\"kick\":' + '\"' + str(event.obj.message['action']['member_id']) + '\"' + "}",
                            "label": "Исключить пользователя"
                        },
                        "color": "negative"
                    }]
                ]
            }

            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))

            vk.method('messages.send', {
                'peer_id': peer_id,
                'message': 'Исключить пользователя?',
                'random_id': 0,
                'keyboard': keyboard
            })
    except:
        pass

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        response = event.obj.message['text'].lower()
        chat_id = int(event.obj.message['peer_id']) - 2000000000
        peer_id = event.obj.message['peer_id']
        if '#Telegram' in event.obj.message['text']:
            try:
                if send_telegram(event.obj.message['text']):
                    SendTestMSG('Сообщение успешно отправлено в телеграм!')
            except Exception as e:
                ExecptionMsgSend(e)
        if '#Discord' in event.obj.message['text']:
            loop = asyncio.get_event_loop()
            try:
                loop.run_until_complete(send_discord(event.obj.message['text']))  # передайте точку входа
                SendTestMSG('Сообщение успешно отправлено в дискорд!')
            except Exception as e:
                ExecptionMsgSend(e)
        KickUser()
        for i in range(len(event.message.attachments)):
            url = event.message.attachments[i]['photo']['sizes'][-1]['url']
            r = requests.get(url, allow_redirects=True)
            open('telegram.jpg', 'wb').write(r.content)

        if event.from_user or event.from_chat and not event.from_group:
            if response.startswith('test'):
                SendTestMSG()
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

        if event.from_user or event.from_chat and CheckIsAdmin():
            if response.startswith('бот нейм') and event.from_chat:
                try:
                    if CheckSecondLine(response) != False:
                        ChatNameChange(chat_id, CheckSecondLine(response))
                    else:
                        SendTestMSG('Вы не ввели название')
                except Exception as e:
                    ExecptionMsgSend(e)
            if response.startswith('бот фото') and event.from_chat:
                try:
                    url = event.message.attachments[0]['photo']['sizes'][-1]['url']
                    r = requests.get(url, allow_redirects=True)
                    open('avatars.jpg', 'wb').write(r.content)

                    res = vk.method('photos.getChatUploadServer', {
                        'chat_id': chat_id,
                    })
                    photo_res = requests.post(res['upload_url'], files={'file': open('avatars.jpg', 'rb')}).json()

                    vk.method('messages.setChatPhoto', {
                        'file': photo_res['response'],
                    })
                except Exception as e:
                    ExecptionMsgSend(e)
            if response.startswith('бот кик') and event.from_chat:
                if event.obj.message['fwd_messages'][0]['from_id'] != event.obj.message['from_id'] and CheckIsAdmin():
                    try:
                        vk.method('messages.removeChatUser', {
                            'chat_id': chat_id,
                            'member_id': event.obj.message['fwd_messages'][0]['from_id']
                        })
                    except Exception as e:
                        SendTestMSG('Произошла ошибка, возможно пользователь является администратором')
                        ExecptionMsgSend(e)
                else:
                    SendTestMSG('Вы не можете себя кикнуть')
            # if response.find('исключить пользователя') and event.from_chat and CheckIsAdmin():
            #     try:
            #         data = json.loads(event.obj.message['payload'])
            #         vk.method('messages.removeChatUser', {
            #             'chat_id': chat_id,
            #             'member_id': data['kick']
            #         })
            #     except:
            #         SendTestMSG('Произошла ошибка.')