from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import os
from dotenv import load_dotenv
import asyncio

async def send_discord(msg, HOOK):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(HOOK, adapter=AsyncWebhookAdapter(session))
        await webhook.send(msg, username='Тот, кто знает домашку')
