import requests
from collections import defaultdict


def max_():
    d = defaultdict(list)
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']
    for name in r:
        d.update({r[name]["Value"]: r[name]["Name"]})

    return d.get(max(d))

max_()