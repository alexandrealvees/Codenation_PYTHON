import requests


def get_temperature(lat, lng):
    key = '38853fa7bad13c5f14b1752b4974837585a48a34'
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)
    reponse = requests.get(url)
    data = reponse.json()
    temperature = data.get('currently').get('temperature')
    if not temperature:

        return
    return int((temperature - 32) * 5.0 / 9.0)
