import logging

import telegram
from telegram import InputMediaPhoto, InputMediaVideo

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def media_group(TELTOKEN, data) -> None:
    logger.info(data)
    bot = telegram.Bot(token=TELTOKEN)
    attachments_list = []

    for i in range(len(data.attachments)):
        if data.attachments[i]['type'] == 'photo':
            if len(attachments_list) < 1:
                attachments_list.append(InputMediaPhoto(data.attachments[i]["photo"]['sizes'][-1]['url'], data.text))
            else:
                attachments_list.append(InputMediaPhoto(data.attachments[i]["photo"]['sizes'][-1]['url']))
        if data.attachments[i]['type'] == 'video':
            # print("typeVi")
            # print(f'https://vk.com/video{data.attachments[i]["video"]["owner_id"]}_{data.attachments[i]["video"]["id"]}')
            # if len(attachments_list) < 1:
            #     attachments_list.append(InputMediaVideo(
            #         f'https://vk.com/video{data.attachments[i]["video"]["owner_id"]}_{data.attachments[i]["video"]["id"]}',
            #         msg))
            # attachments_list.append(InputMediaVideo(
            #     f'https://vk.com/video{data.attachments[i]["video"]["owner_id"]}_{data.attachments[i]["video"]["id"]}'))
            pass

    logging.info(attachments_list)
    bot.send_media_group("-248326565", attachments_list)
    # bot.send_video("-248326565", "https://vk.com/video247155585_456239456")

def msg_without_img(TELTOKEN, data):
    logger.info(data)
    bot = telegram.Bot(token=TELTOKEN)
    bot.send_message('-248326565', data.text)