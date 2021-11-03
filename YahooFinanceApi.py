from os import waitpid
import requests
import time
import json
import csv
from pprint import pprint

url = "https://yfapi.net/v6/finance/quote"

#file with all stock tickers to compare user input to 
file = open(r"c:\Users\Student\OneDrive - University of Virginia\Desktop\College\Fall 2021\DS 3002\TickerSymbols.csv")
reader = csv.reader(file)
list_symbol = []
for row in reader:
    for object in row:
        list_symbol.append(object.lower())

#asking user for symbol input
symbol = input("Please input a stock ticker: ")
value = symbol.lower().strip()

if value in list_symbol:
    querystring = {"symbols": symbol+",BTC-USD,EURUSD=X"}

    headers = {
    'x-api-key': "q9ACqArWFJ1SJq1QW5due7R8dkeQxxVg3HAqIXKU"
    }
    #getting json response and selecting specific values
    response = requests.get(url, headers=headers, params=querystring).json()
    currentPrice = response['quoteResponse']['result'][0]['regularMarketPrice']
    currentTime = response['quoteResponse']['result'][0]['regularMarketTime']
    timeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(currentTime))
    name = response['quoteResponse']['result'][0]['shortName']

    #printing values to console
    print("Current Price: "+str(currentPrice))
    print("Market Time: "+str(timeStamp))
    print("Company Name: "+ name)

    #saving call information to CSV file
    data = [value.upper(), timeStamp, currentPrice]
    with open(r"c:\Users\Student\OneDrive - University of Virginia\Desktop\College\Fall 2021\DS 3002\YahooFinanceCallHistory.csv",'a',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)

#if user input is not valid, it informs users
else:
    print("Not a valid Ticker Symbol")