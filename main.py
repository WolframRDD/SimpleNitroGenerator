import requests
import time
import random, string
from discord import Webhook, RequestsWebhookAdapter

link = input("Введите ссылку на ваш Webhook: ")
amount = int(input("Сколько кодов сгенерировать: "))
for i in range(amount):
    time.sleep(1)
    code = "https://discord.gift/" + "".join(random.choices    (string.ascii_letters + string.digits, k=16))
    print("[Создан] " + code)
    webhook = Webhook.from_url(link, adapter=RequestsWebhookAdapter())
    webhook.send(code)