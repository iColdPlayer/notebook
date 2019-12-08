import json
from urllib.request import urlopen

with urlopen('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json') as resp:

	source = resp.read()

data = json.loads(source)

rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))
