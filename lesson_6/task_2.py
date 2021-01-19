class Road:
    # Asphalt density in kg/(m2*sm), Param_2 is thickness in sm
    __asphalt_density = (25, )
    # Asphalt thickness in sm
    __asphalt_thickness = (5,)

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    # Calculate required asphalt mass in tons
    def get_asphalt_mass(self) -> float:
        return (self.__asphalt_density[0] * self.__asphalt_thickness[0] * self._length * self._width)/1000


new_road = Road(5000, 20)
print(f'Нужно {new_road.get_asphalt_mass():.2f}т асфальта')
