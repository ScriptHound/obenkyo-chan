from typing import Any, Callable
import logging

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
        logging.info("Query successed")

    except Exception:
        session.rollback()
        raise RuntimeError('Query failed')

    finally:
        session.close()

    return result


@bl.message(text=["Дай карточку"])
async def greeting(message: Message):
    symbol = handle_session(HiraganaCard().get_random)
    letter = symbol.original_appearance
    await message.answer(f"Вот держи! {letter}")
