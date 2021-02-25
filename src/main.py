from vkbottle import Bot
from routes.main_router import labelers

bot = Bot("token")

for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)

bot.run_forever()