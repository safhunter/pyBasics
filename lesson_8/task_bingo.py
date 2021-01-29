import random
from abc import ABC, abstractmethod


class BingoCard:
    pass


class AbsPlayer(ABC):
    """ Base class for any player """
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @name.setter
    @abstractmethod
    def name(self, name: str) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_human(self) -> bool:
        raise NotImplementedError

    @is_human.setter
    @abstractmethod
    def is_human(self, flag: bool) -> None:
        raise NotImplementedError


class BingoPlayer(AbsPlayer):
    """Class for bingo player, inherit for Player.
        It takes a bingo cards count, then generate them"""
    def __init__(self, name: str, is_human: bool = True, cards_count: int = 1):
        self._name = ''
        self._is_human = True
        self.name = name
        self.is_human = is_human
        self._cards = []
        self.generate_cards(cards_count)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if name != '':
            self._name = name

    @property
    def is_human(self) -> bool:
        return self._is_human

    @is_human.setter
    def is_human(self, flag: bool) -> None:
        self._is_human = flag

    def generate_cards(self, cards_count: int) -> None:
        cards = []
        if cards_count > 0:
            for i in range(cards_count):
                cards.append(BingoCard())
        self._cards = cards

    def show_cards(self) -> str:
        result = ''
        for card in self._cards:
            result += str(card) + '\n'
        return result
