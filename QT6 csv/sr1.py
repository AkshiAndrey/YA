import csv
import math

yearning = int(input())
with open('main_cities.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter='.', quotechar='"')
    print(reader)
    result = list(filter(lambda x: yearning <= int(int(x[2]) / int(x[3]) * 100), [i for i in reader][1:]))
    print(result)

for i in result:
    print(i[1], f'({int(int(i[2]) / int(i[3]) * 100)})')


print(int(5.6))