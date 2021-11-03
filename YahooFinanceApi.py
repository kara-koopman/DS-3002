from os import waitpid
import requests
import pandas as pd
import time
import json
import csv
from pprint import pprint
from os import path

url = "https://yfapi.net/v6/finance/quote"
savingPath = r'C:\Users\Student'

#file with all stock tickers to compare user input to 
symbolUrl = "https://raw.githubusercontent.com/kara-koopman/DS-3002/main/TickerSymbols.csv"
resp = pd.read_csv(symbolUrl)

#asking user for symbol input
symbol = input("Please input a stock ticker: ")
value = symbol.lower().strip()

if (value in resp):
    print("Ticker symbol is not valid")
else:
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
    try:
        with open(savingPath+'\YahooFinanceCallHistory.csv','a',newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(data)
            print('CSV file is called "YahooFinanceCallHistory.csv" and is saved to C:/Users/Student')
    except: 
        print('Unable to save final CSV document. Please check savingPath')
