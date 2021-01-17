from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
HOOK = os.getenv('HOOK_LINK')
async def send_discord(msg):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(HOOK, adapter=AsyncWebhookAdapter(session))
        await webhook.send(msg, username='Тот, кто знает домашку')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(foo()) # передайте точку входа
    finally:
        # действия на выходе, если требуются
        pass