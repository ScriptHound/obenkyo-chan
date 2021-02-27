from __future__ import annotations
from typing import Dict, List
import random


from models.cards import HiraganaLetter, KatakanaLetter


class Card:
    model_class = None

    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, session, japanese: str, latin: str, cyrrilic: str = "N/A") -> None:
        card = cls(latin, japanese, cyrrilic)
        session.add(card)

    def bulk_create(self, session, letters: List[Dict[str, str]]):
        """cards should be a list of dictionaries"""
        cards = [self.model_class(**letter) for letter in letters]
        session.bulk_save_objects(cards)

    def get(self, session, japanese: str) -> Card:
        card = session.query(self.model_class).filter(
            self.model_class.original_appearance == japanese).one()
        return card

    def get_random(self, session) -> str:
        table_length = session.query(self.model_class).count()
        rand_index = random.randint(1, table_length-1)
        return session.query(
                    self.model_class).filter(
                        self.model_class.id==rand_index).one()

    def delete(self, session, card: str) -> None:
        card = self.get(session, card)
        session.delete(card)


class HiraganaCard(Card):
    model_class = HiraganaLetter


class KatakanaCard(Card):
    model_class = KatakanaLetter
