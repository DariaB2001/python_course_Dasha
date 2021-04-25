class Figure:

    def __init__(self):
        self.color = 'white'

    def change_color(self, new_color):
        if new_color == self.color:
            self.color = new_color
            print('Зачем перекрашивать фигуру в тот же самый цвет??..')
        else:
            self.color = new_color
            print(f'Сейчас цвет фигуры - {self.color}')


    def inform(self):
        raise NotImplementedError


class Oval(Figure):

    def __init__(self, size):  # при создании овала надо задать его размер
        super().__init__()
        self.size = size
        self.name = 'oval'

    def inform(self):
        print(f'Перед вами фигура {self.name} размера {self.size}, которая покрашена в цвет {self.color}')


class Square(Figure):

    def __init__(self, side_lenght):  # при создании овала надо задать его размер
        super().__init__()
        self.side_lenght = side_lenght
        self.name = 'square'

    def inform(self):
        print(f'Перед вами фигура {self.name} площади {self.side_lenght**2}, которая покрашена в цвет {self.color}')


oval1 = Oval('big')
oval1.inform()
oval1.change_color('white')
oval1.change_color('red')
oval1.inform()
square = Square(5)
square.inform()
