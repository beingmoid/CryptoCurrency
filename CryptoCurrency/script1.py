
import datetime

import pandas as pd
import requests
from matplotlib import pyplot as plt


#get historical price of cryptocurrency and return the value
def GetHistoData(to_symbol, from_symbol, type='histohour', all_data=True, limit=1, aggregate=1, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/{}?fsym={}&tsym={}&limit={}&aggregate={}' \
        .format(type, to_symbol.upper(), from_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    if all_data:
        url += '&allData=true'

    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df


#plot the price of crypto currency
def plot_value_in_graph(axis, df, to_symbol, from_from):
    axis.plot(df.timestamp, df.close)
    axis.set_title(to_symbol + ' Vs ' + from_from)
    axis.set_ylabel('Price In ' + from_from)
    axis.set_xlabel('Year')
    print("\n")


data_histomin = GetHistoData('BTC', 'USD', 'histominute')
data_histoday = GetHistoData('BTC', 'USD', 'histoday')
data_histohour = GetHistoData('BTC', 'USD', 'histohour')
f, axes = plt.sudbplots(3)

plot_value_in_graph(axes[0], data_histomin, 'BTC', 'USD')
plot_value_in_graph(axes[1], data_histoday, 'BTC', 'USD')
plot_value_in_graph(axes[2], data_histohour, 'BTC', 'USD')

plt.show()