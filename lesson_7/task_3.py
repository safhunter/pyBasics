class Cell:
    # count: total cells count
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.count + other.count)
        else:
            raise TypeError(f'Argument type is not a {type(self)}')

    def __sub__(self, other):
        if isinstance(other, Cell):
            if self.count >= other.count:
                return Cell(self.count - other.count)
            else:
                raise ValueError(f'Minuend must be greater then subtrahend')
        else:
            raise TypeError(f'Argument type is not a {type(self)}')

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.count * other.count)
        else:
            raise TypeError(f'Argument type is not a {type(self)}')

    def __truediv__(self, other):
        if isinstance(other, Cell):
            if other.count > 0:
                return Cell(round(self.count / other.count))
            else:
                raise ValueError(f'Cant divide by empty cell')
        else:
            raise TypeError(f'Argument type is not a {type(self)}')

    # row_length: Quantity cells in a row
    def make_order(self, row_length: int):
        if row_length > 0:
            template = '*' * row_length + '\n'
            return template*(self.count // row_length) + '*'*(self.count % row_length)
        else:
            raise ValueError(f'Row length must be greater then 0')


cell_1 = Cell(10)
cell_2 = Cell(20)

cell_3 = cell_1 + cell_2
cell_4 = cell_2 - cell_1
cell_5 = cell_1 * cell_2
cell_6 = cell_2 / cell_1

print(f'Cell_3:\n{cell_3.make_order(10)}')
print(f'Cell_4:\n{cell_4.make_order(10)}')
print(f'Cell_5:\n{cell_5.make_order(10)}')
print(f'Cell_6:\n{cell_6.make_order(10)}')
