import sys

import requests


def get_district(address):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        'apikey': "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"
    }
    response = requests.get(geocode_url, params=params)
    data = response.json()
    if data["response"]["GeoObjectCollection"]["metaDataProperty"]["GeocoderResponseMetaData"]["found"] == "0":
        print("Адрес не найден.")
        return

    coordinates = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    lon, lat = coordinates.split()

    district_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        'apikey': "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": f"{lon},{lat}",
        "kind": "district",
        "format": "json"
    }
    response = requests.get(district_url, params=params)
    data = response.json()

    try:
        district = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
            "GeocoderMetaData"]["text"]
        print(f"Адрес '{address}' находится в районе: {district}")
    except:
        print("Не удалось определить район для данного адреса.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Пожалуйста, введите адрес в качестве аргумента командной строки.")
    else:
        address = sys.argv[1]
        get_district(address)
