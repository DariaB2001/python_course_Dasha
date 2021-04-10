import time
t = time.time()
squares = []
for i in range(10):
    squares.append(i**2)
new_time = time.time() - t
with open(time.strftime('%H:%M:%S_%d.%m.%Y' + '.txt'), 'w') as f:
    f.write('На операцию потребовалось ' + str(new_time) + ' секунд')
