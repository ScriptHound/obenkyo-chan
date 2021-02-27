import logging
import random

from vkbottle_types import BaseStateGroup
from vkbottle.bot import Blueprint, Message
from sqlalchemy.orm import session, sessionmaker

from src.queries.queries import HiraganaCard
from src.queries.session_handlers import handle_session
from db_config import engine

logging.basicConfig(level=logging.INFO)
bl = Blueprint()
Session = sessionmaker(bind=engine)


class QuizStates(BaseStateGroup):
    QUIZ_STATE = 0
    FREE_STATE = 1


def create_letters_poll() -> dict:
    letters = [handle_session(HiraganaCard().get_random,
                              Session,
                              engine
                              )for _ in range(4)]

    return {number: letter for number, letter in enumerate(letters)}


def create_poll_template(poll_data: dict) -> str:
    return "\n"+"\n".join(
        [f"{n}. {letter}" for n, letter in poll_data.items()])


@bl.on.message(state=QuizStates.QUIZ_STATE, text=["0", "1", "2", "3"])
async def quiz_handler(message: Message, **args):
    user_answer = args.get("user_answer")
    right_answer = args.get("right_answer")
    print(user_answer, right_answer)
    await bl.state_dispenser.set(message.peer_id, QuizStates.FREE_STATE)
    if user_answer == right_answer:
        await message.answer("Ура ура, правильно!")
    else:
        await message.answer("Неправильно...")


@bl.on.message(text=["Дай карточку"])
async def greeting(message: Message):
    poll: dict = create_letters_poll()
    right_answer_index: int = random.choice(list(poll.keys()))
    right_answer: HiraganaCard = poll[right_answer_index].transcription

    poll = create_poll_template(poll)

    await bl.state_dispenser.set(message.peer_id, QuizStates.QUIZ_STATE)
    await message.answer(f"Я загадала {right_answer}! {poll}")
    return right_answer_index
