# Create a function, standalone or account class
import pandas as pd


def allocateDividends(dividendFile: pd.DataFrame, accounts: list):
    for index, row in dividendFile.iterrows():
        accountNo = row['Account']

        account = next((account for account in accounts if str(account.number) == str(accountNo)), None)

        if account == None:
            print("No account")
            break

        if row['Amount'] > 0:
            account.cashBalance += row['Amount']
        elif row['Units'] > 0:
            unitsToAllocate = row['Units']
            unitsAcrossPortfolios = 0.0

            for goal in account.goals:
                for allocation in goal.portfolio.allocations:
                    if allocation.ticker == row['Symbol']:
                        unitsAcrossPortfolios += allocation.units

            for goal in account.goals:
                for allocation in goal.portfolio.allocations:
                    if allocation.ticker == row['Symbol']:
                        allocation.units += unitsToAllocate * (allocation.units / unitsAcrossPortfolios)


# Show (print) an account level summary of new dividends with date included
spy = yf.Ticker("SPY")
spy.dividends
