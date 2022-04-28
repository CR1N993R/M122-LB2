import datetime
import os
import sys
from fpdf import FPDF

from src.alphaVantage import get_stock_data, get_description
from src.ftp import upload
from src.graphGenerator import create_graph
from src.report import generate_new_page
from src.sendToEmail import send_to_email

timePeriod = ""
stockName = ""
email = ""
ftpUser = ""
ftpAddress = ""
ftpPassword = ""


def check_args():
    if len(timePeriod) > 0 and len(stockName) > 0:
        if timePeriod.lower().endswith("h") or timePeriod.lower().endswith("d"):
            return True
        else:
            print("Invalid time please append H(hours) or D(days) to the end")
    else:
        print("Missing Argument -t or -a")
    return False


def rising(data):
    start = data[list(data.keys())[-1]]["1. open"]
    end = data[list(data.keys())[0]]["4. close"]
    return end > start


def get_diff(data):
    start = data[list(data.keys())[-1]]["1. open"]
    end = data[list(data.keys())[0]]["4. close"]
    return round(float(end) - float(start), 2)


def get_percentage(data):
    diff = get_diff(data)
    start = data[list(data.keys())[-1]]["1. open"]
    return round(diff / float(start) * 100, 2)


def main():
    for index, arg in enumerate(sys.argv):
        if arg == "-a":
            global stockName
            stockName = sys.argv[index + 1]
        elif arg == "-t":
            global timePeriod
            timePeriod = sys.argv[index + 1]
        elif arg == "-e":
            global email
            email = sys.argv[index + 1]
        elif arg == "-u":
            global ftpUser
            ftpUser = sys.argv[index + 1]
        elif arg == "-s":
            global ftpAddress
            ftpAddress = sys.argv[index + 1]
        elif arg == "-p":
            global ftpPassword
            ftpPassword = sys.argv[index + 1]
        else:
            if arg.startswith("-"):
                print("Unknown Option " + arg)
                exit(-1)

    if check_args():
        pdf = FPDF()
        companies = stockName.split(",")
        for company in companies:
            data = get_stock_data(company, timePeriod)
            info = get_description(company)
            if len(info) > 0 and len(data) > 0:
                create_graph(data, company)
                generate_new_page(pdf, info["Description"], company, info["Name"], rising(data), get_percentage(data), get_diff(data))
                os.remove(company + ".png")
        time = datetime.datetime.now()
        filename = time.strftime("%d-%m-%Y %H_%M_%S")
        filename = filename + " " + stockName + ".pdf"
        pdf.output(filename, "F")
        upload(filename, ftpAddress, ftpUser, ftpPassword)
        send_to_email(email, filename)


if __name__ == '__main__':
    main()
