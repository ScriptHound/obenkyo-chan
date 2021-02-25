from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, Unicode
Base = declarative_base()


class HiraganaLetter(Base):
    __tablename__ = 'hiragana_cards'

    id = Column('id', Integer, primary_key=True)
    transcription = Unicode(length=5)
    cyrillic = Unicode(length=5)
    original_appearance = Unicode(length=1)

    def __init__(self,
        transcription: str,
        original_appearance: str,
        cyrrilic: str) -> None:

        self.transcription = transcription
        self.original_appearance = original_appearance
        self.cyrillic = cyrrilic
