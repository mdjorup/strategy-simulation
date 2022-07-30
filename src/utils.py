import requests
import json

import yfinance

class Stock:

    def __init__(self, data, dividends):

        
        pass



def load_data(symbol: str, period: str = '1y'):

    stock = yfinance.Ticker(symbol)


    hist = stock.history(period=period)

    data = []

    for index, row in hist.iterrows():

        item = {
            "date": str(index),
            "open": row["Open"],
            "high": row["High"],
            "low": row["Low"],
            "close": row["Close"],
            "dividend": row["Dividends"]
        }
        data.append(item)


    return data 

    
    

load_data("AAPL", '1mo')
