import http.client
import json


def getDescription(stock_name):
    conn = http.client.HTTPSConnection("www.alphavantage.co")
    conn.request("GET", "/query?function=OVERVIEW&symbol=" + stock_name + "&apikey=$FXI1M9JI1IYPL04R")
    data = conn.getresponse().read().decode("utf-8")
    data = json.loads(data)
    return data["Description"]


def getStockData(stock_name):
    conn = http.client.HTTPSConnection("www.alphavantage.co")
    conn.request("GET", "/query?function=TIME_SERIES_DAILY&symbol=" + stock_name + "&apikey=$FXI1M9JI1IYPL04R")
    data = conn.getresponse().read().decode("utf-8")
    data = json.loads(data)
    print(list(data.keys())[0])
    for datum in data["Time Series (Daily)"]:
        print(data["Time Series (Daily)"][datum])
    return data
