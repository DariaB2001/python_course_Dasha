class Person:

    def __init__(self, name, age, passport_data):
        self.name = name
        self.__age = age
        self.__passport_data = passport_data

    def change_age(self, age):
        if self.__age <= age:
            self.__age = age
            print(f'Теперь Ваш возраст - {self.__age}')
        else:
            print('Нельзя расти вниз, можно только вверх')

    def change_name(self, new_name):
        if self.__age > 17:
            self.name = new_name
            print(f'Теперь Ваше имя - {self.name}')
        else:
            print('Ты ещё маленький и не можешь менять имя, поэтому смирись.')

    def change_passport_data(self, new_passport_data):
        if self.__age == 20 or self.__age == 45:
            self.__passport_data = new_passport_data
            print(f'Теперь Ваши паспортные данные - {self.__passport_data}')
        else:
            print('Паспорт в нашей стране меняют в 20 и в 45 лет, так что потерпите')


girl = Person('Галя', 17, 501435988)
girl.change_name('Эрика')
girl.change_age(15)
girl.change_age(22)
girl.change_name('Эрика')
girl.change_passport_data(3546778899)
girl.change_age(45)
girl.change_passport_data(1234567890)
