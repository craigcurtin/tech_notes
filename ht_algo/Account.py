#import Portfolio
#import Order
from TransactionType import TransactionType
import logging
import json
import os.path

class AccountType(object):
    def __init__(self, value: str):
        logging.info(f'AccountType: {value}')
        if value not in ("Taxable", "Roth IRA", "Traditional IRA"):
            raise ValueError("Allowed types: Taxable, Roth IRA, Traditional IRA")
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class AccountStatus(object):
    def __init__(self, value: str):
        if not value in ("PENDING", "IN_REVIEW", "APPROVED", "REJECTED", "SUSPENDED"):
            raise ValueError("Allowed statuses: PENDING, IN_REVIEW, APPROVED, REJECTED, SUSPENDED")
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class Account(object):
    #def __init__(self, number: str, accountType: AccountType, accountStatus: AccountStatus, cashBalance: float = 0.0):
    def __init__(self, number: str, accountType: AccountType):
        self.goals = []
        self.account_number = number
        #self.cashBalance = cashBalance
        self.accountType = accountType
        #self.accountStatus = accountStatus
        self.holdings = self.load_holdings(self.account_number)

    def load_holdings(self, account_num):
        '''load_holdings - input: account number, return: dict of holdings'''
        account_file = os.path.abspath(f'Data/{account_num}_holdings.json')
        logging.info(f'load_holdings: {account_file}')

        with open(account_file, "r") as read_file:
            json_data = json.load(read_file)
        return json_data
    def value(self):
        ''' provide value of holdings a this time ...'''
        return 1.0
    def get_tickers(self):
        '''iterate through holdings, return tickers (NO duplicates)'''
        print (self.holdings)
        ticker_set = set()
        for holding in self.holdings:
            ticker_set.add(holding['ticker'])
        logging.info(f'get_tickers(): {ticker_set}')
        return ticker_set
    def get_positions(self):
        '''get_positions() returns a list of holdings (Ticker/Quantity)'''
        positions_set = set()
        for holding in self.holdings:
            positions_set.add( ( holding['ticker'], float(holding['quantity'] )) )

        logging.info(f'get_positions(): {positions_set}')
        return positions_set


# pip install pandas_market_calendars
