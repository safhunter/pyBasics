class Matrix:
    def __init__(self, data: list, filler: int = 0):
        self.data = data
        self.filler = filler
        self.row_count = len(data)
        self.column_count = 0
        for row in self.data:
            row_length = len(row)
            if row_length > self.column_count:
                self.column_count = row_length
        self.extend()

    def extend(self, row_count: int = None, column_count: int = None):
        r_count = row_count or self.row_count
        c_count = column_count or self.column_count
        for i in range(r_count):
            if i >= self.row_count:
                self.data.append([])
            self.data[i].extend([self.filler for i in range(c_count - len(self.data[i]))])

    def __str__(self):
        result = ''
        for row in self.data:
            result += '\t'.join(map(str, row)) + '\n'
        return result

    def __add__(self, other):
        if isinstance(other, Matrix):
            if other.row_count == self.row_count and other.column_count == self.column_count:
                result_list = []
                for i, row in enumerate(self.data):
                    result_list.append([])
                    for j, item in enumerate(row):
                        result_list[i].append(item + other.data[i][j])
                return Matrix(result_list)
            else:
                raise ValueError('Matrices must be the same dimensions')
        else:
            raise TypeError(f'Argument is no a type {type(self)}')


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8]])
print(f'Matrix_1 \n{matrix_1}')
matrix_2 = Matrix([[1, 1, 1], [], []], 1)
print(f'Matrix_2 \n{matrix_2}')
matrix_3 = matrix_1 + matrix_2
print(matrix_3)
