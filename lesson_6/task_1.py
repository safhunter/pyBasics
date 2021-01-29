from itertools import cycle
from time import sleep
import keyboard
from threading import Thread


class TrafficLight:
    # Red, Yellow, Green
    __colors = (0xFF0000, 0xFFFF00, 0x00FF00)
    __color_names = ('Red', 'Yellow', 'Green')

    def __init__(self, green_timing: int = None):
        self.__color = self.__colors[0]
        self.__timings = [7, 2, 5]
        if green_timing is not None:
            self.set_green_timing(green_timing)

    def get_color(self):
        return self.__color

    def get_color_name(self):
        return self.__color_names[self.__colors.index(self.__color)]

    # set timing for green light in seconds
    def set_green_timing(self, timing: int):
        self.__timings[2] = timing

    def running(self):
        for i, item in cycle(enumerate(self.__colors)):
            self.__color = item
            print(self.get_color_name())
            sleep(self.__timings[i])


traffic_light = TrafficLight(10)
print(f'Для завершения нажмите Esc')
traffic_thread = Thread(target=traffic_light.running, daemon=True)
traffic_thread.start()
keyboard.wait('Esc')
exit()

