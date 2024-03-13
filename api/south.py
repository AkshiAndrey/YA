import sys

import requests


def get_coord(city_):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        'apikey': "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": city_,
        "format": "json"
    }
    response = requests.get(geocode_url, params=params)
    data = response.json()
    if data["response"]["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"]["found"] == "0":
        return

    coordinates = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    lon, lat = coordinates.split()
    cities_.append([city_, lat])


if __name__ == "__main__":
    cities_ = []
    cities = input('Введите список городов через запятую:\n').split(',')
    for city in cities:
        get_coord(city)
    cities_.sort(key=lambda x: float(x[1]))
    # print(cities_)
    print(f'Самый южный город из перечисленных: {cities_[0]}')
