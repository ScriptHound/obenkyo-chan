from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer, UnicodeText
Base = declarative_base()


class Card:
    id = Column('id', Integer, primary_key=True)
    transcription = Column(UnicodeText)
    cyrillic = Column(UnicodeText)
    original_appearance = Column(UnicodeText, unique=True)

    def __init__(self,
        transcription: str,
        original_appearance: str,
        cyrrilic: str) -> None:

        self.transcription = transcription
        self.original_appearance = original_appearance
        self.cyrillic = cyrrilic


class HiraganaLetter(Base, Card):
    __tablename__ = 'hiragana_cards'


class KatakanaLetter(Base, Card):
    __tablename__ = 'katakana_cards'
