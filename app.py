# Currency Exchange
import inline as inline
import matplotlib
import pandas
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import regression
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import linear_model

# API used: https://exchangerate.host/#/#docs
#
# print("ENTER THREE LETTER CURRENCY CODE WHEN PROMPTED ie USD or EUR")
# print("")
# currency_code1 = input("From currency code: ")
# currency_code2 = input("To currency code: ")
# amount = input("Amount: ")
# url = 'https://api.exchangerate.host/convert'
# response = requests.get(url, params={
#     "from": currency_code1,
#     "to": currency_code2,
#     "amount": amount,
#     "places": 2
# })
# data = response.json()['result']
# print("Result: ",end="")
# print(data)
# print("")
#
# print("Historical data - first 10 months for reference")
currency_data = pd.read_csv("GBPUSD=X-2yr.csv")
print(currency_data.head(10))
print("")

# plot data from CSV file
axis = sns.scatterplot(x="Date", y="Close", data=currency_data)
# rotate dates
plt.xticks(rotation=-40)

# title
plt.title("USD - Exchange rate 1 year")

# train data
x = currency_data[["Open", "High", "Low"]]
# target data
y = currency_data["Close"]

# return NumPy ndarray
x = x.to_numpy()
y = y.to_numpy()

# training
xtrain, xtest,ytrain, ytest = train_test_split(x,y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
md = LinearRegression()
md.fit(xtrain,ytrain)

reg = linear_model.LinearRegression()
reg.fit(xtrain,ytrain)

# Display predictions
print("Next 5 predictions: ")
pre = reg.predict(xtest)
print(pre)

print("")
print("Testing to see how close the predictions are: ")
print("Predicting next currency rate will be: ")
print(pre[0])
print("Actual next currency rate for 2017-11-1 is: ")
print(ytrain[0])



# Use data from Open, High and Low to train
close_prediction = md.predict(xtest)

print("")

print("Another prediction: ")
print("Predict currency for the next 5 days: ")
currency_data = pd.DataFrame(data={"Prediction": close_prediction.flatten()})

# print predicted data
print(currency_data.head())

# display graph
plt.show()

