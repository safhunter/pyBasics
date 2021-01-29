class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction: str):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} {self.speed}км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Машина {self.name} превысила допустимую скорость 60км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Машина {self.name} превысила допустимую скорость 60км/ч')


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, True)


police = PoliceCar(90, 'B&W', 'Dodge')
car_1 = WorkCar(30, 'Gray', 'VW Caddy')
car_2 = SportCar(150, 'Red', 'Ferrari')
car_3 = TownCar(200, 'Black', 'Zaz', False)

police.show_speed()
car_1.show_speed()
car_2.show_speed()
car_3.show_speed()

print(f'Цвет первой машины:{car_1.color}')

car_1.go()
car_2.stop()
car_3.turn('в лес')
