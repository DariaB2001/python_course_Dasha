class BankAccount:

    def __init__(self, name, account_number, balance, password):
        self.name = name
        self.account_number = account_number  # публичные атрибуты имя владельца и номер счёта
        self.__balance = balance
        self.__password = password  # приватные атрибуты баланс и пароль

    def set_balance(self, balance, password):
        if self.__password == password:
            self.__balance = balance
            print(f'Теперь баланс вашего счёта - {str(self.__balance)}')
        else:
            print('Неверный пароль, попробуйте ещё раз')

    def get_balance(self, password):
        if self.__password == password:
            print(f'Баланс вашего счёта - {str(self.__balance)}')
            return self.__balance
        else:
            print('Вы самозванец, мы вам не скажем баланс счёта')

    def info(self):
        print(f'Имя владельца счёта: {self.name};\nНомер счёта: {self.account_number}')


account = BankAccount("Pablo", 12345678, 100000, 'ku*3')
account.info()
account.get_balance('ku*1')
account.get_balance('ku*3')
account.set_balance(120000, 'kjfdhk')
account.set_balance(120000000, 'ku*3')
