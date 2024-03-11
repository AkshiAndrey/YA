import csv

ans = dict()
school, class_ = map(int, input().split())
with open('rez.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    strings = sorted([x for x in reader][1:], key=lambda x: int(x[7]), reverse=True)
    for m in strings:
        login = m[2][12:].split('-')
        if int(login[0]) == school and int(login[1]) == class_:
            if m[7] in ans:
                ans[m[7]].append(m[1].split()[3])
            else:
                ans[m[7]] = [m[1].split()[3]]

for m in ans:
    for n in sorted(ans[m], reverse=True):
        print(n, m)