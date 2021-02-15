def season(number):
    winter = [1, 2, 12]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]
    if number in winter:
        season = 'Зима'
    if number in spring:
        season = 'Весна'
    if number in summer:
        season = 'Лето'
    if number in autumn:
        season = 'Осень'
    return print(season)


season(1)
season(8)
