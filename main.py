import logging
import os
from vkhelper.vk import vkbot
from dotenv import load_dotenv

import vk_api
from vk_api.bot_longpoll import *

logging.basicConfig(filename='logs/app.log', filemode='w', format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger(__name__)

def main():
    logger.info("Bot started")
    load_dotenv()
    VKTOKEN = os.getenv('VK_TOKEN')
    TELTOKEN = os.getenv('TELE_TOKEN')
    HOOK = os.getenv('HOOK_LINK')

    # Connect vk
    vk = vk_api.VkApi(token=VKTOKEN)
    vk._auth_token()
    vk.get_api()
    longpool = VkBotLongPoll(vk, 182910634)

    vkbot.vk_start(longpool, vk, HOOK, TELTOKEN)

if __name__ == "__main__":
    main()