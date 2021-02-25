from os import getenv
from vkbottle import Bot
from src.routes import labelers

bot = Bot(getenv("TOKEN"))

for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)

bot.run_forever()
