import sys
from src.alphaVantage import *

timePeriod = ""
stockName = ""
email = ""
ftpUser = ""
ftpAddress = ""
ftpPort = 0
ftpPassword = ""


def check_args():
    if len(timePeriod) > 0 and len(stockName) > 0:
        print(getDescription(stockName))
        (getStockData(stockName))
    else:
        print("Missing Argument -t or -a")


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
            global ftpPort
            ftpPort = sys.argv[index + 1]
        elif arg == "-P":
            global ftpPassword
            ftpPassword = sys.argv[index + 1]
        else:
            if arg.startswith("-"):
                print("Unknown Option " + arg)
                exit(-1)
    check_args()


if __name__ == '__main__':
    main()
