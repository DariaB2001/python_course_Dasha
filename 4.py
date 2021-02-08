word = input('Введите текст: ')
list = []
for i in range(len(word)):
    if word[i] != ' ':
        list.append(word[i].lower())
n = 0
for i in range(len(list)):
    if list[i] == list[len(list) - i - 1]:
        n = 1
    else:
        n = 0
        break
if n == 1:
    print('Последовательность является палиндромом')
else:
    print('Последовательность не является палиндромом')
