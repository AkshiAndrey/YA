from pprint import pprint

m = 4
n = 7

result1, result2, result3 = 3, 4, 5
total = result1 + result2 + result3

if total >= n and all((map(lambda x: x >= m, (result1, result2, result3)))):
    print(0)



for i in map(lambda x: x >= m, (result1, result2, result3)):
    print(i)