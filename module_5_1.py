class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # [print(i) for i in range(1, new_floor +1) if 1 <= new_floor <= self.number_of_floors else print("Такого этажа не существует")]
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)

        else:
            print("Такого этажа не существует")


House('ЖК Эльбрус', 30)
h1 = House('ЖК Горский', 18)
# print(h1.name, h1.number_of_floors)
h2 = House('Домик в деревне', 2)
# print(h2.name, h2.number_of_floors)
h1.go_to(5)
h2.go_to(10)
