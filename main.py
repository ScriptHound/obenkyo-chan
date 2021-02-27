from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from vkbottle.bot import Bot
from src.routes.middlewares import OnAnswerMiddleware
from src.routes.return_managers import QuizAnswerReturnHandler

from src.routes import blueprints

env_path = Path('.') / 'config/.env'
load_dotenv(dotenv_path=env_path)

bot = Bot(getenv("TOKEN"))

for blueprint in blueprints:
    blueprint.load(bot)

bot.labeler.message_view.handler_return_manager = QuizAnswerReturnHandler()
bot.labeler.message_view.register_middleware(OnAnswerMiddleware())
bot.run_forever()
