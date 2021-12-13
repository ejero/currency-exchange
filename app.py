import inline as inline
import matplotlib
import requests
import os
from pprint import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import regression



# API used: https://exchangerate.host/#/#docs

print("ENTER THREE LETTER CURRENCY CODE WHEN PROMPTED ie USD or EUR")
print("")
currency_code1 = input("From currency code: ")
currency_code2 = input("To currency code: ")
amount = input("Amount: ")
url = 'https://api.exchangerate.host/convert'
response = requests.get(url, params={
    "from": currency_code1,
    "to": currency_code2,
    "amount": amount,
    "places": 2
})
data = response.json()['result']
print("Result: ",end="")
print(data)
print("")
print("Historical data")

currency_data = pd.read_csv("GBPUSD=X-monthly.csv")
print(currency_data.head())


# plot data from CSV file
axis = sns.lineplot(x="Date", y="Close", data =currency_data)
plt.xticks(rotation=45)
plt.show()

