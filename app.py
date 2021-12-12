import requests
import sys
from pprint import pprint


# API used: https://exchangerate.host/#/#docs

print("ENTER THREE DIGIT CURRENCY SYMBOL WHEN PROMPTED ie USD or EUR")
print("")
currency_symbol1 = input("From currency symbol: ")
currency_symbol2 = input("To currency symbol: ")
amount = input("Amount: ")
url = 'https://api.exchangerate.host/convert'
response = requests.get(url, params={
    "from": currency_symbol1,
    "to": currency_symbol2,
    "amount": amount,
    "places": 2
})
data = response.json()['result']
print("result: ",end="")
pprint(data)