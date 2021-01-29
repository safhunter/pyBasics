from abc import ABC, abstractmethod, abstractproperty


class AbsClothes(ABC):
    @abstractproperty
    def cloth_consumption(self):
        pass


class Coat(AbsClothes):
    # Size EU
    def __init__(self, size: float):
        self.size = size

    @property
    def cloth_consumption(self):
        return self.size/6.5 + 0.5


class Suit(AbsClothes):
    # Height in meters
    def __init__(self, height: float):
        self.height = height

    @property
    def cloth_consumption(self):
        return self.height*2 + 0.3


my_coat = Coat(52)
my_suit = Suit(1.76)
print(f'Нужно {my_coat.cloth_consumption + my_suit.cloth_consumption:.2f} погонных метров ткани')
