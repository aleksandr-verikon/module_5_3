class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if 1 > new_floor or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


h1 = House('"ТаймСквер"', 33)
h2 = House('"База StarKiller"', 33)
h1.go_to(18)
h2.go_to(34)
print(h1)
print(h2)

print(len(h1))
print(len(h2))

print(h1 == h2) #33 == 33 True
print(h1 < h2) #33 < 33 False
print(h1 > h2) #33 > 33 False
print(h1 <= h2) #33 <= 33 True
print(h1 >= h2) #33 >= 33 True
print(h1 != h2) #33 != 33 False
h1 = h1 + 7 #33 + 7 = 40
print(h1)
print(h1 == h2) #40 == 33 False
h1 += 1  # увеличивает количество этажей на 1
print(h1)
h1 = 2 + h1  # тоже увеличивает количество этажей на 2
print(h1)