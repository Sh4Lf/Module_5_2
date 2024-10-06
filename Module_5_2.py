class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        title = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return title


hightower = House('ЖК Немчиновка', 19)
warehouse = House('Гаражи', 5)

print(hightower)
print(warehouse)

print(len(hightower))
print(len(warehouse))