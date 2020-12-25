class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person_1 = Person("Миша", 10)
person_2 = Person("Егор", 10)

test_list = [person_1.age, person_2.age]

for item in test_list:
    print(type(item))
    print(id(item))
