from __future__ import annotations
from models.cards import HiraganaLetter, KatakanaLetter

class Card:
    model_class = None

    def create(self, session, japanese: str, latin: str, cyrrilic: str = "N/A") -> None:
        card_class = self.__class__
        card = card_class.__init__(latin, japanese, cyrrilic)
        session.add(card)

    def get(self, session, japanese: str) -> Card:
        card = session.query(self.model_class).filter(
            self.model_class.original_appearance == japanese).one()
        return card

    def delete(self, session, card: str) -> None:
        card = self.get(session, card)
        session.delete(card)


class HiraganaCard(Card):
    model_class = HiraganaLetter

class KatakanaCard(Card):
    model_class = KatakanaLetter
