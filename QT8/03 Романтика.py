# Вводится начальная дата, затем строки вида:
# <работа>, <день недели, в который работа выполняется>, <общий объем>, <выполнение за день>
# Один день – одна работа.
# Начиная с введенного дня, выведите даты, для которых есть работа, и до тех пор,
# пока вся работа не будет выполнена.
# Формат вводимых и выводимых дат: MM.DD.YYYY. После даты через пробел
# выведите работу и в скобках количество, выполненное в этот день.

import sys
import datetime as dt

date = dt.datetime.strptime(input(), '%m.%d.%Y')
d = {}
for line in sys.stdin:
    tmp = line.strip().split(', ')
    d[int(tmp[1])] = [tmp[0], int(tmp[2]), int(tmp[3])]
while True:
    k = date.weekday()
    if k in d and d[k][1] > 0:
        s = d[k][1] if d[k][2] >= d[k][1] else d[k][2]
        print(f'{date.strftime("%m.%d.%Y")} {d[k][0]} ({s})')
        d[k][1] -= s
    date += dt.timedelta(days=1)
    task = 0
    for x in d:
        task += d[x][1] > 0
    if task == 0:
        break
