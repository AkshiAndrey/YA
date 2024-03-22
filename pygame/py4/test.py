from pprint import pprint

# lab = []
# rdl = list(map(int, input().split()))
# n = rdl[0]
# m = rdl[1]
for i in range(n):
        rdl = input()
        stroka = []
        for k in range(m):
            if int(rdl[k]) == 1:
                stroka.append(-1)
            else:
                stroka.append(int(rdl[k]))
        lab.append(stroka)

def voln(x, y, cur, n, m, lab):
    lab[x][y] = cur
    if y + 1 < m:
        if lab[x][y + 1] == 0 or (lab[x][y + 1] != -1 and lab[x][y + 1] > cur):
            voln(x, y + 1, cur + 1, n, m, lab)
    if x + 1 < n:
        if lab[x + 1][y] == 0 or (lab[x + 1][y] != -1 and lab[x + 1][y] > cur):
            voln(x + 1, y, cur + 1, n, m, lab)
    if x - 1 >= 0:
        if lab[x - 1][y] == 0 or (lab[x - 1][y] != -1 and lab[x - 1][y] > cur):
            voln(x - 1, y, cur + 1, n, m, lab)
    if y - 1 >= 0:
        if lab[x][y - 1] == 0 or (lab[x][y - 1] != -1 and lab[x][y - 1] > cur):
            voln(x, y - 1, cur + 1, n, m, lab)

    return lab


voln(2, 0, 0, m, n, lab)
for i in lab:
    print(i)


#
