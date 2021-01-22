import logging
import os
from vkhelper.vk import vkbot
from dotenv import load_dotenv

import vk_api
from vk_api.bot_longpoll import *

logger = logging.getLogger(__name__)

def main():
    logger.info("Bot started")
    load_dotenv()
    TOKEN = os.getenv('VK_TOKEN')

    # Connect vk
    vk = vk_api.VkApi(token=TOKEN)
    vk._auth_token()
    vk.get_api()
    longpool = VkBotLongPoll(vk, 182910634)

    vkbot.vk_start(longpool, vk)

if __name__ == "__main__":
    main()