class Box:

    def __init__(self, size):
        self.size = size  # максимальное количество объектов, которые можно сложить в коробку
        self.content = []  # содержание коробки - изначально коробка пустая

    def print_info(self):
        print(f'В эту коробку можно положить {self.size} объектов, сейчас в ней лежат следующие объекты: {",".join(self.content)}')

    def ad_object(self, object):
        if len(self.content) < self.size:
            self.content.append(object.name)
            print('вы положили в коробку ' + object.name)
        else:
            print('Эта коробка уже полная до конца:(')


class Circle:

    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.name = 'circle'


class Square:

    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.name = 'sqare'


class Triangle:

    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.name = 'triangle'


class Rectangle:

    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.name = 'rectangle'


box = Box(3)
box.print_info()
circle = Circle('big', 'red')
triangle = Triangle('small', 'yellow')
square = Square('very big', 'black')
rectangle = Rectangle('very small', 'green')
box.ad_object(circle)
box.ad_object(triangle)
box.ad_object(square)
box.print_info()
box.ad_object(rectangle)
