from sys import stdin

for i in stdin.readlines():
    with open(i[:-1], 'r', encoding='utf-8') as file:
        name = i[:-5]
        sr_1 = sorted(map(int, [j.strip() for j in file.readlines()[::2]]), reverse=True)[:5]
        first_value = round(sum(sr_1) / len(sr_1), 1)
        file.seek(0)
        sr_2 = sorted(map(int, [j.strip() for j in file.readlines()[1::2]]), reverse=True)[:5]
        secont_value = round(sum(sr_2) / len(sr_2), 1)
        with open('stranger.txt', 'a', encoding='utf-8') as file_2:
            file_2.write(', '.join((name + ' ' + 'tram', str(first_value), str(secont_value) + '\n')))
