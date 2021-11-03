from os import waitpid
import requests
import time
import json
import csv
from pprint import pprint
from os import path

url = "https://yfapi.net/v6/finance/quote"

#file with all stock tickers to compare user input to 
savingPath = r'C:\Users\Student\OneDrive - University of Virginia\Desktop\College\Fall 2021\DS 3002'

if path.exists(savingPath):
    fileName = '\TickerSymbols.csv'
    try:
        file = open(savingPath + fileName)
        reader = csv.reader(file)
        list_symbol = []
        for row in reader:
            for object in row:
                list_symbol.append(object.lower())
    except:
        raise Exception("Could not create symbol list from CSV file")
else:
    print("File path does not exist: Please update program's savingPath variable for the proper saving destination on computer")
    print('File path should be the same as the location where "TickerSymbols.csv" is stored')
    exit()

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
    try:
        with open(savingPath+'\YahooFinanceCallHistory.csv','a',newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(data)
            print('CSV file is called "YahooFinanceCallHistory.csv" and is saved in the same location as the "TickerSymbol.csv" file')
    except: 
        print('Unable to save final CSV document. Please check savingPath')

#if user input is not valid, it informs users
else:
    print("Not a valid Ticker Symbol")