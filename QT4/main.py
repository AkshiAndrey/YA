def total_size(sizes):
    dct_ = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4}
    lst = ['B', 'KB', 'MB', 'GB', 'TB']
    res = 0
    max_unit = 'B'
    for size, unit in sizes:
        res += size * 1024 ** dct_[unit]
        max_unit = max(max_unit, unit, key=lambda x: dct_[x])
    res /= 1024 ** dct_[max_unit]
    while res > 1023:
        res /= 1024
        max_unit = lst[lst.index(max_unit) + 1]
        # for key, value in dct_.items():
        #     if value - 1 == dct_[max_unit]:
        #         max_unit = key
    return f'{round(res)} {max_unit}'


d = {}
for line in open('input.txt').readlines():
    name, size, unit = line.split()
    _, ext = name.split('.')
    d.setdefault(ext, list()).append((name, int(size), unit))

f = open('output.txt', 'w')
f.close()
for ext, arr in sorted(d.items(), key=lambda x: x[0]):
    names = []
    sizes = []
    for name, size, unit in arr:
        names.append(name)
        sizes.append((size, unit))
    with open('output.txt', 'a') as f:
        for name in sorted(names):
            f.write(f'{name}\n')
        f.write('----------\n')
        f.write(f'Summary: {total_size(sizes)}\n\n')
