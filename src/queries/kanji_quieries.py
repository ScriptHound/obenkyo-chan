from __future__ import annotations

from models.cards import Card
from models.kanji_cards import (
    KanjiCard,
    JapReading,
    Meaning
)


class KanjiQueries(Card):
    model_class = KanjiCard

    # returns to session
    def create(self,
               session: 'Session',
               kanji: str,
               reading: str,
               meaning: str,
               grade: int) -> KanjiCard:
        kanji = KanjiCard(reading, kanji, "", meaning, grade)
        session.add(kanji)


class MeaningQueries:

    def create(self, session: 'Session', meaning: str) -> Meaning:
        session.add(Meaning(meaning))

    def get(self, session: 'Session', meaning: str) -> Meaning:
        meaning = session.query(Meaning).filter(
            Meaning.meaning == meaning).one()

        return meaning

    def delete(self, session: 'Session', meaning: str):
        meaning = self.get(session, meaning)
        session.delete(meaning)


class JapReadingQueries:
    def create(self, session: 'Session', reading: str) -> JapReading:
        session.add(JapReading(reading))

    def get(self, session: 'Session', reading: str) -> JapReading:
        reading = session.query(JapReading).filter(
            JapReading.reading == reading).one()

        return reading

    def delete(self, session: 'Session', reading: str):
        reading = self.get(session, reading)
        session.delete(reading)
