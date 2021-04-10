import time


def ask_time(number):
    if number > 0:
        time.sleep(number)
        ask_time(number=int(input('Введите, пожалуйста, целое число: ')))
    elif number < 0:
        pass


ask_time(number=int(input('Введите, пожалуйста, целое число: ')))
