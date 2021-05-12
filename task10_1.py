class Girl:

    def __init__(self, name, age, number_of_husbands):
        self.name = name  # своё имя девочка говорит всем
        self._age = age  # возраст скрывает
        self.__number_of_husbands = number_of_husbands  # количество мужей - это ваще секрет


ann = Girl('Ann', 33, 5)
print(ann.name)
print(ann._age)
print(ann.__number_of_husbands)
