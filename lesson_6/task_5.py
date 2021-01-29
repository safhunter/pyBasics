class Stationery:
    def __init__(self, title: str = ''):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручки')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандаша')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркера')


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
