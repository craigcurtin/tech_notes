import os.path
import sys
import pandas as pd
import utils
import logging
from Account import Account
from Account import AccountType

import traceback
import sys
import utils

from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from datetime import datetime
from datetime import timedelta
from MarketData import MarketData

def main(argc, argv):

    accounts = {}
    taxable_account = None
    for account_number in [ '1234', '5678'] :
        taxable_account = AccountType("Taxable")
        accounts[account_number] = Account(account_number, taxable_account )
    logging.info(f'Accounts: {accounts},')

    for account_number in [ '8765' ]:
        taxable_account = AccountType("Traditional IRA")
        accounts[account_number] = Account(account_number, taxable_account )
    logging.info(f'Accounts: {accounts},')

    for account_number in ['4321']:
        taxable_account = AccountType("Roth IRA")
        accounts[account_number] = Account(account_number, taxable_account )
    logging.info(f'Accounts: {accounts},')

    # now we have our accounts and positions ....
    set_of_tickers = set()
    for account in accounts.keys():
        for t in accounts[account].get_tickers():
            set_of_tickers.add(t)
    logging.info(f'Need to get Market Data for Tickers: {set_of_tickers}')

    # now we have our Tickers, go get Market for Tickers
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    duration_days = 365
    duration = timedelta(days=duration_days)
    start = yesterday - duration
    start_date = f"{start.year}-{start.month}-{start.day}"
    #end_date = f"{datetime.today().year}-{datetime.today().month}-{datetime.today().day}"
    end_date = f"{yesterday.year}-{yesterday.month}-{yesterday.day}"

    logging.info(f'Market Data start: {start_date}, end: {end_date}')

    # process the command line args ....
    marketdata = {}

    for ticker in set_of_tickers:
        #marketdata_file = os.path.abspath(f'tests/resources/{yesterday.year}-{yesterday.month}-{yesterday.day}_{ticker}.csv')
        # ... save in a temporary locatoin, /tmp gets cleaned up ...
        marketdata_file = os.path.abspath(f'/tmp/{yesterday.year}-{yesterday.month}-{yesterday.day}_{ticker}.csv')
        if os.path.exists(marketdata_file) :
            marketdata[ticker] = open(marketdata_file).readlines()
        else:
            try:
                # file is not present, go get Market Data and persist to file
                marketdata[ticker] = MarketData(ticker, start_date, end_date)
                with open(marketdata_file, 'w') as fd:
                    fd.write(marketdata[ticker].get_data().to_csv())
            except Exception as err:
                logging.exception(traceback.format_exc())
                logging.exception(sys.exc_info()[2])
        # done getting all the MArketdata we need ...

    # now we have: AccountInfo, Marketdata ... easy to provide valuation on a specific day
    for account in accounts.keys():
        for tuple in accounts[account].get_positions():
            ADJ_CLOSE_PRICE = 6
            try:
                logging.info(f'Ticker: {tuple[0]} Qty: {tuple[1]}')
                md = marketdata[tuple[0]][1]
                logging.debug(f'MD --> [{md[:-1]}]')
            except IndexError as ex:
                logging.exception(f'NO MARKET DATA FOR Ticker: {tuple[0]}')
                continue
            try:
                adj_close = float(md.split(',')[ADJ_CLOSE_PRICE])/100000
                value = adj_close * tuple[1]
                # note .... for Value, insert the "," as a thousands separator in the printing the float
                logging.info (f'Account: #{account}, Holding: {tuple[0]},\tQuantity: {tuple[1]},\tPrice: ${adj_close},\tValue: ${value:,.3f}')
            except IndexError as ex:
                logging.exception(md)
                logging.exception(f'Holding: {tuple[0]},\tQuantity: {tuple[1]},\tPrice: $0,\tValue: $0')


    # # Calculate expected returns and sample covariance
    # mu = expected_returns.mean_historical_return(df)
    # S = risk_models.sample_cov(df)
    #
    # # Optimize for maximal Sharpe ratio
    # ef = EfficientFrontier(mu, S)
    # raw_weights = ef.max_sharpe()
    # cleaned_weights = ef.clean_weights()
    # ef.save_weights_to_file("weights.csv")  # saves to file
    # print(cleaned_weights)
    # ef.portfolio_performance(verbose=True)

    return
if __name__ == '__main__' :
    exe_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    utils.setup_logger(exe_name, '/tmp', logging.INFO)
    main(len(sys.argv), sys.argv)