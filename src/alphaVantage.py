import http.client
import json
from time import sleep


def send_request(args, stock_name):
    conn = http.client.HTTPSConnection("www.alphavantage.co")
    conn.request("GET", "/query?" + args + "&symbol=" + stock_name + "&apikey=$FXI1M9JI1IYPL04R")
    data = conn.getresponse().read().decode("utf-8")
    if "Note" in data:
        sleep(61)
        return send_request(args, stock_name)
    return json.loads(data)


def get_description(stock_name):
    data = send_request("function=OVERVIEW", stock_name)
    if "Description" in data and "Symbol" in data:
        return data
    return ""


def get_stock_data_hourly(stock_name):
    data = send_request("function=TIME_SERIES_INTRADAY&interval=60min", stock_name)
    if "Time Series (60min)" in data:
        return data["Time Series (60min)"]
    return ""


def get_stock_data_daily(stock_name):
    data = send_request("function=TIME_SERIES_DAILY", stock_name)
    if "Time Series (Daily)" in data:
        return data["Time Series (Daily)"]
    return ""


def get_stock_data(stock_name, time):
    if time.endswith("H"):
        data = get_stock_data_hourly(stock_name)
    else:
        data = get_stock_data_daily(stock_name)
    if len(data) > 0:
        time = int(time[:-1])
        indexes = list(data)[:time]
        data = dict((k, data[k]) for k in indexes)
        return data
    return ""

