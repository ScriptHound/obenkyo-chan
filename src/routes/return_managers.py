from vkbottle import BaseReturnManager
from vkbottle.bot import Message
from caches.main import cache


class QuizAnswerReturnHandler(BaseReturnManager):
    @BaseReturnManager.instance_of(int)
    async def right_answer_handler(self, value: int, message: Message, _: dict):
        cache.set(message.from_id, value)
