string = input()
list = string.split(' ')
d = []
for i in range(len(list)):
    n = 0
    for j in range(len(list)):
        if list[i] == list[j]:
            n += 1
    if n > 1:
        d.append(1)
    else:
        d.append(0)
if 1 in d:
    print('В последовательности есть дубликаты')
else:
    print('В последовательности нет дубликатов')
