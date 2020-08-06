import os
from actions.login import Login
import requests
from utils.constants import *
from utils.optionPnl import *
from utils.helpers import *
from tda import client
import mibian

def main():
    t = Login()

    algolist = t.get_watchlist(ACCOUNT_ID, ALGOLIST_ID).json()['watchlistItems']

    for asset in algolist:
        symbol = asset['instrument']['symbol']
        quote = t.get_quote(symbol).json()
        fundamentalEnum = t.Instrument.Projection.FUNDAMENTAL
        fund = t.search_instruments(symbol, fundamentalEnum).json()[symbol]['fundamental']
        paysDividends = fund['dividendDate'] != ' '
        beta = fund['beta']
        print(fund)
        vol10DayAvg = fund['vol10DayAvg']
        historyDays = 90
        hv = historicalVolatility(t, symbol, 90)
        # mibian.BS([Underlying Price, Call / Price Strike Price, Interest Rate, Days To Expiration], Call / Put Price)
        iv = mibian.BS([51.04, 51, 0, 2], callPrice=.58).impliedVolatility
        print(iv)
        break

if __name__ == '__main__':
    main()
