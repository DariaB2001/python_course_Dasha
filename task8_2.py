class Instruments:

    def __init__(self, name, type, volume):
        self.name = name
        self.type = type
        self.volume = volume

    def print_info(self):
        print(f'Это музыкальный инструмент {self.name}, он принадлежит к группе {self.type}, громкий он примерно так: {self.volume}')


violin = Instruments('скрипка', 'струнные', 'поначалу кажется, что громко, но потом привыкаешь')
flute = Instruments('флейта', 'деревянные духовые', 'низкие звуки ничего, зато высокие слышно на другом конце улицы')
drums = Instruments('барабаны', 'ударные', 'пусть лучше музыкант тренируется на подушках')
violin.print_info()
flute.print_info()
drums.print_info()
