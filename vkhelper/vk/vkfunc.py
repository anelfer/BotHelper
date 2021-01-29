import vk_api
import asyncio

from vkhelper.discord.discordbot import send_discord
from vkhelper.telegram.telegrambot import media_group

class VkFunc():

    def __init__(self, vk, chat_id, peer_id, from_id):
        self.vk = vk
        self.peer_id = peer_id
        self.chat_id = chat_id
        self.from_id = from_id

    def chat_name_change(self, chat_id, name):
        try:
            self.vk.method('messages.editChat', {
                'chat_id': chat_id,
                'title': name
            })
            self.send_given_msg('Название успешно изменено')
        except:
           self.send_given_msg('Произошла непредвиденная ошибка.')

    def execption_msg_send(self, e):
        self.vk.method('messages.send', {
            'peer_id': self.peer_id,
            'message': e,
            'random_id': 0
        })

    def send_given_msg(self, message='Тестовое cообщение'):
        self.vk.method('messages.send', {
            'peer_id': self.peer_id,
            'message': message,
            'random_id': 0
        })

    def check_second_line(self, response):
        if response.find('\n') != -1:
            return response[response.find('\n')::]
        return None

    def check_is_admin(self):
        check = self.vk.method('messages.getConversationMembers', {
            'peer_id': self.peer_id,
        })
        for i in check['items']:
            if i['member_id'] == self.from_id:
                admin = i.get('is_admin', False)
                if admin == True:
                    return True
        return False

    def forward_to(self, msg, HOOK, TELTOKEN, data):
        if '#Tel' in msg:
            try:
                media_group(TELTOKEN, data)
                self.send_given_msg('Сообщение успешно отправлено в телеграм!')
            except Exception as e:
                self.execption_msg_send(e)

        if '#Dis' in msg:
            loop = asyncio.get_event_loop()
            try:
                loop.run_until_complete(send_discord(msg, HOOK))  # передайте точку входа
                self.send_given_msg('Сообщение успешно отправлено в дискорд!')
            except:

                self.execption_msg_send("Произошла непредвиденная ошибка!")