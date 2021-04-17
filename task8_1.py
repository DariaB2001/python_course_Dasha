class Man:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'name: {self.name}, age: {self.age}')

    def feed(self, pet):
        if pet.hunger == True:
            pet.hunger = False
            print('Теперь ваш питомец счастлив! Но ненадолго')
        else:
            print('Почему-то ваш питомец не голоден. Возможно, он сожрал корм другого кота. Будьте внимательнее!')


class Cat:

    def __init__(self, name):
        self.hunger = True  # кот по определению всегда голодный
        self.name = name

    def print_info(self):
        print(self.name)
        if self.hunger == True:
            print('Котик очень голодный!!!')
        else:
            print('Отстань от меня, ничтожный, чего тебе нужно')


man = Man('Paul', 20)
man.print_info()
cat = Cat('Microcat')
cat.print_info()
man.feed(cat)  # покормим кота
cat.print_info()
man.feed(cat)  # попробуем покромить сытого кота
