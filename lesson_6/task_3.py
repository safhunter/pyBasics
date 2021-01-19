class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict()
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


ivanov = Position('Ivan', 'Ivanov', 'Manager', 10000, 30000)
petrov = Position('Alexey', 'Petrov', 'Manager', 20000, 32000)
smith = Position('John', 'Smith', 'Boss', 100000, 300000)

print(f'{ivanov.position} {ivanov.get_full_name()} total income {ivanov.get_total_income()}$')
print(f'{petrov.position} {petrov.get_full_name()} total income {petrov.get_total_income()}$')
print(f'{smith.position} {smith.get_full_name()} total income {smith.get_total_income()}$')