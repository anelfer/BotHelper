import vk_api

from vkhelper.discord.discordbot import send_discord
# from vkhelper.discord.discordbot import send_dis_img

from vkhelper.telegram.telegrambot import media_group
from vkhelper.telegram.telegrambot import msg_without_img


class VkFunc:

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

    def exception_msg_send(self, e):
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
                if admin:
                    return True
        return False

    def forward_to(self, HOOK, TELTOKEN, data):
        if '#Tel' in data.text:
            try:
                if len(data.attachments) >= 1:
                    media_group(TELTOKEN, data)
                    self.send_given_msg('Сообщение успешно отправлено в телеграм с фото!')
                else:
                    msg_without_img(TELTOKEN, data)
                    self.send_given_msg('Сообщение успешно отправлено в телеграм без фото!')
            except Exception as e:
                self.exception_msg_send(e)

        if '#Dis' in data.text:
            try:
                send_dis_img(data, HOOK)
                self.send_given_msg('Сообщение успешно отправлено в дискорд!')
            except Exception as e:
                self.exception_msg_send(e)
                self.send_given_msg(data.text)
