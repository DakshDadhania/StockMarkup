## fetch live stock price and store in CSV file
import sys
import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import date
from datetime import datetime
import nsetools
from nsetools import Nse
def fetch_NSE_stock_price(stock_code):
    
    stock_url  = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stock_code)
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(stock_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")
    for item in data_array:
        if 'lastPrice' in item:
            index = data_array.index(item)+1
            latestPrice=data_array[index].split('"')[1]
            return float(latestPrice.replace(',',''))
    
n=input("Enter stock code")
fetch_NSE_stock_price(n)
