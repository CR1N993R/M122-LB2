import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def print_bars(plt, index, close, high, low, open, stick1, stick2, body):
    plt.bar(index, close - open, .4, bottom=open, color=body)
    plt.bar(index, high - stick1, .05, bottom=stick1, color="black")
    plt.bar(index, low - stick2, .05, bottom=stick2, color="black")


def create_graph(data, company):
    print("Generating graph for company: " + company + "...")
    prices = pd.DataFrame.from_dict(data, "index")
    prices["1. open"] = prices["1. open"].astype(float)
    prices["2. high"] = prices["2. high"].astype(float)
    prices["3. low"] = prices["3. low"].astype(float)
    prices["4. close"] = prices["4. close"].astype(float)
    prices.index = pd.to_datetime(prices.index)

    up = prices[prices["4. close"] >= prices["1. open"]]
    down = prices[prices["4. close"] < prices["1. open"]]

    plt.figure()
    print_bars(plt, up.index, up["4. close"], up["2. high"], up["3. low"], up["1. open"], up["4. close"], up["1. open"], "green")
    print_bars(plt, down.index, down["4. close"], down["2. high"], down["3. low"], down["1. open"], down["1. open"], down["4. close"], "red")

    plt.xticks(rotation=45, ha='right', fontsize=14)
    plt.yticks(fontsize=14)
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(17, 10)

    plt.savefig(company + ".png", bbox_inches="tight")
    print("Done.")
