from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, UnicodeText
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table

from models.cards import Card
from models.base import Base
###
# Kanji has many meanings and many readings which also has many kanjis
###


association_table = Table('association',
                          Base.metadata,
                          Column("kanji_id", Integer, ForeignKey("kanji.id")),
                          Column("meaning_id", Integer, ForeignKey("meaning.id"))
                          )


jap_reading_associate = Table('jap_reading_assoc',
                              Base.metadata,
                              Column('kanji_id', Integer, ForeignKey("kanji.id")),
                              Column('reading_id', Integer, ForeignKey('reading.id'))
                              )


class KanjiCard(Card, Base):
    __tablename__ = 'kanji'
    grade = Column(Integer)
    meanings = relationship("Meaning",
                            secondary=association_table,
                            back_populates="kanjis"
                            )
    readings = relationship("JapReading",
                            secondary=jap_reading_associate,
                            back_populates="kanjis"
                            )

    def __init__(self,
                 transcription: str,
                 original_appearance: str,
                 cyrrilic: str,
                 meaning: str,
                 grade: int
                 ) -> None:
        super().__init__(transcription, original_appearance, cyrrilic)
        self.meaning = meaning
        self.grade = grade


class Meaning(Base):
    __tablename__ = "meaning"
    id = Column('id', Integer, primary_key=True)
    meaning = Column('meaning', UnicodeText)
    kanjis = relationship("KanjiCard",
                          secondary=association_table,
                          back_populates="meanings"
                          )


class JapReading(Base):
    __tablename__ = "reading"
    id = Column('id', Integer, primary_key=True)
    reading = Column('reading', UnicodeText)
    kanjis = relationship("KanjiCard",
                          secondary=jap_reading_associate,
                          back_populates="readings"
                          )
