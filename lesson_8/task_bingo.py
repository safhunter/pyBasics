import random
from abc import ABC, abstractmethod


class BingoCard:
    """ Class for bingo card.
    When instance created, it generate a bingo card as 2dim list of random int [1-90] without duplicates.
    Total 15 number for 5 in a row, other places filled with 0
    __PASSED_NUMBER_FILLER must be less then 0
    """
    __PASSED_NUMBER_FILLER = (-1,)

    @staticmethod
    def __get_number_key(number: int) -> int:
        if number == 90:
            return 8
        else:
            return number // 10

    @classmethod
    def __replace_symbols(cls, number: int) -> str:
        if number == 0:
            return ' '
        elif number == cls.__PASSED_NUMBER_FILLER[0]:
            return '-'
        else:
            return str(number)

    @classmethod
    def __generate(cls) -> []:
        init_list = [x for x in range(1, 91)]
        result_card = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        count = 0
        while count < 15:
            init_index = random.randrange(0, len(init_list))
            value = init_list[init_index]
            key = cls.__get_number_key(value)
            for i in range(3):
                if result_card[i][key] > 0 or result_card[i].count(0) < 5:
                    if result_card[i][key] > value:
                        if (result_card[1][key] == 0 and result_card[i].count(0) > 4) or result_card[2][key] == 0:
                            result_card[i][key], value = value, result_card[i][key]
                    continue
                result_card[i][key] = value
                init_list.pop(init_index)
                count += 1
                break
        return result_card

    def __init__(self):
        self._numbers = self.__generate()

    def __str__(self) -> str:
        result = '-------------------------------------\n'
        for line in self._numbers:
            tmp_str = '\t|'.join(map(self.__replace_symbols, line))
            result += '|' + tmp_str + '\t|\n'
        result += '-------------------------------------'
        return result

    def pass_number(self, number: int) -> None:
        for i, line in enumerate(self._numbers):
            try:
                self._numbers[i][line.index(number)] = self.__PASSED_NUMBER_FILLER[0]
                return
            except ValueError:
                continue
        return

    def have_number(self, number: int) -> bool:
        for i, line in enumerate(self._numbers):
            try:
                return line.index(number) >= 0
            except ValueError:
                continue
        return False

    def is_empty(self):
        for line in self._numbers:
            for num in line:
                if num > 0:
                    return False
        return True


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
    default_player_count = 0

    def __init__(self, name: str = None, is_human: bool = True, cards_count: int = 1):
        self._name = ''
        self._is_human = True
        if name is None:
            BingoPlayer.default_player_count += 1
            self.name = f'Аноним {BingoPlayer.default_player_count}'
        else:
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
            result += str(card)
        return result

    @property
    def cards(self) -> []:
        return self._cards

    def have_number(self, number: int) -> bool:
        for card in self.cards:
            if card.have_number(number):
                return True
        return False

    def pass_number(self, number: int) -> bool:
        result = False
        for card in self.cards:
            if card.pass_number(number):
                result = True
        return result

    def ask_number(self, number: int) -> bool:
        if self.is_human:
            answer = True if input(f'Зачеркнуть цифру? (y/n):').lower() == 'y' else False
        else:
            answer = self.have_number(number)
        return answer

    def have_empty_card(self):
        for card in self._cards:
            if card.is_empty():
                return True
        return False


class BingoGame:
    """ Bingo game
    It takes a list of players
    """

    def __init__(self, players: []):
        self.__numbers = [x for x in range(1, 91)]
        self._players = []
        for player in players:
            if isinstance(player, BingoPlayer):
                self._players.append(player)
        self.winners = []
        self.losers = []

    def __get_new_number(self) -> int:
        return self.__numbers.pop(random.randrange(len(self.__numbers)))

    def __new_round(self):
        active_number = self.__get_new_number()
        print(f'Новый бочонок: {active_number} (осталось {len(self.__numbers)})')
        i = 0
        while i < len(self._players):
            player = self._players[i]
            print(f'Ход игрока {player.name}:\nБочонок: {active_number}. Его карточка(и):')
            print(player.show_cards())
            player_answer = player.ask_number(active_number)
            player_result = player.have_number(active_number)
            if player_answer != player_result:
                self.losers.append(self._players.pop(i))
                print(f'Игрок {player.name} проиграл и выбывает из игры')
            else:
                if player_result:
                    player.pass_number(active_number)
                    if player.have_empty_card():
                        self.winners.append(player)
                i += 1

    def play(self):
        print(f'Новая игра!\nСписок участников:')
        for player in self._players:
            print(f'{player.name}\n')
        while len(self._players) > 1 and not self.winners:
            self.__new_round()
        if not self.winners:
            self.winners.append(self._players[0])
        print(f'Игра окончена!\nПобедил(и):')
        for winner in self.winners:
            print(f'{winner.name}\n')


players = [BingoPlayer(), BingoPlayer(is_human=False)]
game = BingoGame(players)
game.play()
