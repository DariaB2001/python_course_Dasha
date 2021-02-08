def season(number):
    winter = [1, 2, 12]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]
    if number in winter:
        season = 'зима'
    if number in spring:
        season = 'весна'
    if number in summer:
        season = 'лето'
    if number in autumn:
        season = 'осень'
    return print(season)


season(1)
season(8)
