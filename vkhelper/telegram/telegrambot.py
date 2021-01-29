import logging

import telegram
from telegram import InputMediaPhoto, InputMediaVideo

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def media_group(TELETOKEN, data) -> None:
    bot = telegram.Bot(token=TELETOKEN)

    bot.send_video(-248326565, video="https://vk.com/video247155585_456239456")
