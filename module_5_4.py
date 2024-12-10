from gevent.subprocess import value


class House():
    houses_history = []  # Атрибут класса для хранения истории зданий

    def __new__(cls, name, *args):
        # Создаем новый объект
        instance = super().__new__(cls)
        cls.houses_history.append(name)
        return instance


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        # Печатаем сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории.")

    def go_to(self, new_floor):
        print(f"Заходим в лифт '{self.name}'")
        if 1 <= new_floor <= self.number_of_floors:
            print(f"Перемещаемся по этажам '{self.name}'...")
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует.")
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: '{self.name}', кол-во этажей: '{self.number_of_floors}'"
    def __eq__(self, other):
        return self.number_of_floors == other
    def __lt__(self, other):
        return self.number_of_floors < other
    def __le__(self, other):
        return self.number_of_floors <= other
    def __gt__(self, other):
        return self.number_of_floors > other
    def __ge__(self, other):
        return self.number_of_floors >= other
    def __ne__(self, other):
        return self.number_of_floors != other
    def __add__(self, value):
        return self.number_of_floors + value
    def __radd__(self, value):
        return self.number_of_floors + value
    def __iadd__(self, value):
        return self.number_of_floors + value


h1 = House("ЖК Эльбрус", 10)
print(House.houses_history)

h2 = House("ЖК Акация", 20)
print(House.houses_history)

h3 = House("ЖК Матрёшка", 20)
print(House.houses_history)  # Выводим историю зданий

del h2
del h3

print(House.houses_history)
