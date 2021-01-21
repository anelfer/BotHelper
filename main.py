import logging
import os
from vkhelper.vk import vk
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

def main():
    logger.error("Bot started")
    load_dotenv()
    TOKEN = os.getenv('VK_TOKEN')

    # Connect vk
    vko = vk_api.VkApi(token=TOKEN)
    vko._auth_token()
    vko.get_api()
    longpool = VkBotLongPoll(vko, 182910634)



if __name__ == "__main__":
    main()