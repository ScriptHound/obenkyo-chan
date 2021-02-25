import csv
from inspect import getfullargspec
import logging

from sqlalchemy.orm import session, sessionmaker

from models.cards import Card
from src.queries.queries import HiraganaCard, KatakanaCard
from db_config import engine

logging.basicConfig(level=logging.INFO)
Session = sessionmaker(bind=engine)
INIT_ARGS = 0


def load_characters(filepath: str) -> list:
    chars_dict = []
    latin_arg_name = getfullargspec(Card.__init__)[INIT_ARGS][1]
    original_appearance_name = getfullargspec(Card.__init__)[INIT_ARGS][2]

    with open(filepath, newline='') as csvfile:
        hirareader = csv.reader(csvfile, delimiter=',')
        for row in hirareader:
            chars_dict.append({latin_arg_name: row[0], original_appearance_name: row[1]})
    return chars_dict


if __name__ == '__main__':
    hira: list = load_characters('src/sources/hiragana.csv')
    kata: list = load_characters('src/sources/katakana.csv')

    conn = engine.connect()
    session = Session(bind=conn)

    try:
        HiraganaCard().bulk_create(session, hira)
        KatakanaCard().bulk_create(session, kata)

        session.commit()
        logging.info("Import successed")
    except Exception:
        session.rollback()
        raise RuntimeError('CSV import failure')

    finally:
        session.close()