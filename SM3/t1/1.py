import csv
import json


def extract_wishes(wishes_file):
    witchcraft = []

    with open(wishes_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter='_')

        for row in csv_reader:
            wishes = [row['wish1'], row['wish2'], row['wish3']]
            if all([len(wish.split()) <= 3 for wish in wishes]):
                witchcraft.append({'name': row['name'], 'age': row['age']})

    with open('witchcraft.json', 'w', encoding='utf-8') as output_file:
        json.dump(witchcraft, output_file, ensure_ascii=False, indent=4)


extract_wishes('wishes.csv')
