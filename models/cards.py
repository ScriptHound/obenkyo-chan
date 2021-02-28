from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import Integer, UnicodeText

from models.base import Base


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

    def __repr__(self):
        return f"""<Letter
                    original_appearance={self.original_appearance},
                    transcription={self.transcription}
                    >"""

    def __str__(self):
        return str(self.original_appearance)


class HiraganaLetter(Base, Card):
    __tablename__ = 'hiragana_cards'


class KatakanaLetter(Base, Card):
    __tablename__ = 'katakana_cards'
