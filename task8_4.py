class Passenger:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.tickets = []  # изначально у пассажиров нет никаких билетов

    def print_info(self):
        print(f'пассажир {self.name}, баланс: {self.money}, купленные билеты: {",".join(self.tickets)}')

    def buy_ticket(self, ticket):  # функция "купить билет"
        if self.money >= ticket.price and ticket.how_many != 0:  # если у пассажира достаточно денег для покупки билета
            # и если билеты вообще есть
            self.tickets.append(ticket.where)
            self.money -= ticket.price
            ticket.how_many -= 1
            print('Поздравляю, вы приобрели билет на поезд ' + ticket.where + ', ваш баланс: ' + str(self.money))
            print(f'Осталось {str(ticket.how_many)} билетов на поезд {ticket.where}')
        else:
            print(f'К сожалению, у пассажира {self.name} недостаточно денег для покупки билета {ticket.where}')

    def return_ticket(self, ticket):  # функция "сдать билет"
        if ticket.where in self.tickets:
            self.tickets.remove(ticket.where)
            self.money += ticket.price
            ticket.how_many += 1
            print(f'Вы только что сдали ваш билет {ticket.where}, ваш баланс: {self.money}, '
                  f'осталось {ticket.how_many} билетов {ticket.where}')
        else:
            print('Извините, но вообще-то вы такого билета не покупали. Сначала купите, а потому уж сдавайте!')


class Ticket:

    def __init__(self, price, where, how_many):
        self.price = price
        self.where = where
        self.how_many = how_many


person1 = Passenger('Петя', 5000)
person1.print_info()
person2 = Passenger('Вася', 3000)
person2.print_info()
ticket_to_moscou = Ticket(4500, 'в Москву', 45)
person1.buy_ticket(ticket_to_moscou)
person1.print_info()
person2.buy_ticket(ticket_to_moscou)
ticket_to_irkutsk = Ticket(1700, 'в Иркутск', 50)
person1.buy_ticket(ticket_to_irkutsk)
person2.buy_ticket(ticket_to_irkutsk)
person2.print_info()
person1.return_ticket(ticket_to_moscou)
person1.buy_ticket(ticket_to_irkutsk)
person2.return_ticket(ticket_to_moscou)
