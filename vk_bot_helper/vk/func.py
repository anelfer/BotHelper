class vk_bot_func():
    def chat_name_change(self, chat_id, name):
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

    def execption_msg_send(self, e):
        vk.method('messages.send', {
            'peer_id': event.obj.message['peer_id'],
            'message': e,
            'random_id': 0
        })

    def send_given_msg(self, message='Тестовое cообщение'):
        vk.method('messages.send', {
            'peer_id': peer_id,
            'message': message,
            'random_id': 0
        })

    def check_second_line(self, response):
        if response.find('\n') != -1:
            return response[response.find('\n')::]
        return None

    def check_is_admin(self):
        check = vk.method('messages.getConversationMembers', {
            'peer_id': peer_id,
        })
        for i in check['items']:
            if i['member_id'] == event.obj.message['from_id']:
                admin = i.get('is_admin', False)
                if admin == True:
                    return True
        return False

    def forward_to(self, msg):
        if '#Tel' in msg:
            try:
                send_telegram(msg)

                send_given_msg('Сообщение успешно отправлено в телеграм!')
            except Exception as e:
                execption_msg_send(e)
        if '#Dis' in msg:
            loop = asyncio.get_event_loop()
            try:
                loop.run_until_complete(send_discord(msg))  # передайте точку входа
                send_given_msg('Сообщение успешно отправлено в дискорд!')
            except Exception as e:
                execption_msg_send(e)
