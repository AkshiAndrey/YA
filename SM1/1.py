result = []
with open('hippocat.txt', 'r', encoding='utf-8') as file:
    for i in file.readlines()[0].split('; '):
        result.extend(map(str.title, i.split()))

result = set(result)

with open('marks.txt', 'w', encoding='utf-8') as file:
    for i in result:
        file.write(i.title() + '\n')
