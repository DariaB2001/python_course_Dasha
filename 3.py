number = input()
list_of_numbers = []
for i in range(len(number)):
    list_of_numbers.append(int(number[i]))
new_number = 0
for i in range(len(list_of_numbers)):
    new_number += list_of_numbers[i]
print(new_number)
