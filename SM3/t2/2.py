import json
from pprint import pprint

import requests

with open('solace.json', 'r') as file:
    config = json.load(file)

host = config.get('host')
port = config.get('port')
words = config.get('words')
max_length = config.get('long')

response = requests.get(f'http://{host}:{port}')
data = json.loads(response.text)
pprint(data)
for i in data:
    print(i)
    print(data[i])

selected_books = [book for book in data if any(word in book for word in words) and len(book) <= max_length and len(book.split(' ')) > len(data[book])]
selected_books.sort()

for book in selected_books:
    print(book)
