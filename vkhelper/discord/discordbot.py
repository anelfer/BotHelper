from discord_webhook import DiscordWebhook


def send_discord(data, HOOK):
    if len(data.attachments) >= 1:
        pass
    else:
        webhook = DiscordWebhook(url=HOOK, content=data.text, username="Тот, кто знает домашку")
        webhook.execute()