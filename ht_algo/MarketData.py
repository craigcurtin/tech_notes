from pandas_datareader import data as pdr
import yfinance as yf
# https://github.com/ranaroussi/yfinance
import traceback
import sys
import logging

class MarketData(object):
    def __init__ (self, ticker, start_date, end_date):
        #"SPY", start = "2017-01-01", end = "2017-04-30"
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

        yf.pdr_override()  # <== that's all it takes :-)
        try:
            # download dataframe
            self.data = pdr.get_data_yahoo(self.ticker, self.start_date, self.end_date)
        except Exception as err:
            logging.exception(traceback.format_exc())
            logging.exception(sys.exc_info()[2])
    def get_data(self):
        return self.data
    def get_ticker(self):
        return self.ticker