class Table:

    def __init__(self, l, w, h):
        self.long = l  # длина
        self.width = w  # ширина
        self.height = h  # высота

    def outing(self):
        print(self.long, self.width, self.height)  # печатаем длину, ширину, высоту стола


class Kitchen(Table):

    def howplaces(self,n):
        if n < 2:
            print ("It is not kitchen table")  # если мест за столом меньше двух, то это не кухонный стол
        else:
            self.places = n  # количество мест за столом равно n

    def outplaces(self):
        print (self.places)  # печатаем количество мест за данным кухонным столом


class Worker(Table):

    def __init__(self, l, w, h):
        super().__init__(l, w, h)
        self.things_on_the_table = []  # вещи, которые лежат на столе

    def inform(self):
        if len(self.things_on_the_table) == 0:
            print('На вашем столе ничего не лежит')
        else:
            print(f'На вашем столе {" ".join(self.things_on_the_table)}')

    def put_chair(self, height):
        if height <= self.height - 0.3:
            print('Вы поставили стул к своему рабочему столу, сядьте уже наконец и работайте!')
        else:
            print('Извините, этот стул слишком высокий для вашего рабочего стола, идите в магазин и купите другой стул.')

    def add_laptop(self, length, width):
        if length <= self.long and width <= self.width:
            self.things_on_the_table.append('ноутбук')
            print('Вы поставили на свой рабочий стол ноутбук, садитесь и работайте уже наконец!')
        else:
            print('Извините, этот ноутбук слишком большой для вашего рабочего стола:(')


    def how_places(self, n):
        if n > 1:
            print('Вдвоём у вас работать точно не получится, этот стол скорее кухонный, поэтому выпейте чаю.')
        else:
            print('Всё нормально, вам никто не будет мешать работать.')


t_room1 = Kitchen(2,1,0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplaces()
t_2 = Table(1,3,0.7)
t_2.outing()
t_work = Worker(2, 1.5, 1)
t_work.inform()
t_work.put_chair(0.7)
t_work.add_laptop(0.5, 0.3)
t_work.inform()
