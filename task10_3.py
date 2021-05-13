class Smartphone:

    def __init__(self, owner, password):
        self.owner = owner
        self.__password = password
        self.number_of_photos = 0
        self.blocking = True  # по умолчанию телефон заблокирован

    def __unblock(self, password):
        if self.__password == password:
            self.blocking = False  # блокировка снята

    def take_photo(self, password):
        self.__unblock(password)
        if not self.blocking:  # если телефон разблокирован
            self.number_of_photos += 1  # тогда сфотографировать
        else:  # если телефон заблокирован
            print('Неверный пароль, вы не можете фотографировать')  # тогда сфотографировать не получится


phone = Smartphone('Kate', 'open')
print(phone.number_of_photos)
phone.take_photo('fjkkdfj')
phone.take_photo('open')
print(phone.number_of_photos)
