from typing import Any, Callable
import logging
import random

from vkbottle.bot import BotLabeler, Message
from sqlalchemy.orm import session, sessionmaker

from ..queries.queries import HiraganaCard, KatakanaCard
from db_config import engine

logging.basicConfig(level=logging.INFO)
bl = BotLabeler()
Session = sessionmaker(bind=engine)


def handle_session(query: Callable, *args) -> Any:
    conn = engine.connect()
    session = Session(bind=conn)
    result = None

    try:
        result = query(*args, session=session)
        session.expunge_all()

        session.commit()

    except Exception:
        session.rollback()
        raise RuntimeError('Query failed')

    finally:
        session.close()

    return result


def create_letters_poll() -> dict:
    letters = [handle_session(HiraganaCard().get_random)
                                      for _ in range(4)]
    return {number: letter for number, letter in enumerate(letters)}


@bl.message(text=["Дай карточку"])
async def greeting(message: Message):
    poll: dict = create_letters_poll()
    right_answer: HiraganaCard = random.choice(poll).transcription

    poll = "\n"+"\n".join(
        [f"{n}. {letter}" for n, letter in poll.items()])
    await message.answer(f"Я загадала {right_answer}! {poll}")
