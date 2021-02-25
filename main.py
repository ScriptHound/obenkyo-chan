from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from vkbottle.bot import Bot

from src.routes import labelers

env_path = Path('.') / 'config/.env'
load_dotenv(dotenv_path=env_path)

bot = Bot(getenv("TOKEN"))

for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)

bot.run_forever()
