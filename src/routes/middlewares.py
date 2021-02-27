from vkbottle import BaseMiddleware
from vkbottle.bot import Message
from src.routes.learn_from_transcript import QuizStates
from caches.main import cache


class OnAnswerMiddleware(BaseMiddleware):
    async def pre(self, message: Message, **kwargs):
        if message.state_peer is not None:
            if message.state_peer.state == QuizStates.QUIZ_STATE:
                right_answer = cache.get(message.from_id).decode()
                return {'user_answer': message.text, 'right_answer': right_answer}
