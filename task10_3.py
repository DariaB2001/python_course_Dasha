class Smartphone:

    def __init__(self, owner, password):
        self.owner = owner
        self.__password = password
        self.number_of_photos = 0

    def __unblock(self, password):
        global blocking
        if self.__password == password:
            blocking = False  # блокировка снята
        else:
            blocking = True  # телефон заблокирован

    def take_photo(self, password):
        self.__unblock(password)
        if blocking == True:
            self.number_of_photos += 1
        else:
            print('Неверный пароль, вы не можете фотографировать')


phone = Smartphone('Kate', 'open')
print(phone.number_of_photos)
phone.take_photo('fjkkdfj')
phone.take_photo('open')
print(phone.number_of_photos)
