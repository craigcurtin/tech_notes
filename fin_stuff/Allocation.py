import yfinance as yf
import pandas as pd


class Allocation(object):
    def __init__(self, ticker, percentage):
        self.ticker = ticker
        self.percentage = percentage
        self.units = 0.0


class Portfolio(object):

    def __init__(self, tickerString: str, expectedReturn: float, portfolioName: str, riskBucket: int):

        self.name = portfolioName
        self.riskBucket = riskBucket
        self.expectedReturn = expectedReturn
        self.allocations = []

        from pypfopt.efficient_frontier import EfficientFrontier
        from pypfopt import risk_models
        from pypfopt import expected_returns

        df = self.__getDailyPrices(tickerString, "20y")

        mu = expected_returns.mean_historical_return(df)
        S = risk_models.sample_cov(df)

        ef = EfficientFrontier(mu, S)

        ef.efficient_return(expectedReturn)
        self.expectedRisk = ef.portfolio_performance()[1]
        portfolioWeights = ef.clean_weights()

        for key, value in portfolioWeights.items():
            newAllocation = Allocation(key, value)
            self.allocations.append(newAllocation)

    def __getDailyPrices(self, tickerStringList, period):
        data = yf.download(tickerStringList, group_by="Ticker", period=period)
        data = data.iloc[:, data.columns.get_level_values(1) == "Close"]
        data = data.dropna()
        data.columns = data.columns.droplevel(1)
        return data

    def printPortfolio(self):
        print("Portfolio Name: " + self.name)
        print("Risk Bucket: " + str(self.riskBucket))
        print("Expected Return: " + str(self.expectedReturn))
        print("Expected Risk: " + str(self.expectedRisk))
        print("Allocations: ")
        for allocation in self.allocations:
            print("Ticker: " + allocation.ticker + ", Percentage: " + str(allocation.percentage))

    @staticmethod
    def getPortfolioMapping(riskToleranceScore, riskCapacityScore):
        import pandas as pd
        allocationLookupTable = pd.read_csv('./Data/Risk Mapping Lookup.csv')
        matchTol = (allocationLookupTable['Tolerance_min'] <= riskToleranceScore) & (
                    allocationLookupTable['Tolerance_max'] >= riskToleranceScore)
        matchCap = (allocationLookupTable['Capacity_min'] <= riskCapacityScore) & (
                    allocationLookupTable['Capacity_max'] >= riskCapacityScore)
        portfolioID = allocationLookupTable['Portfolio'][(matchTol & matchCap)]
        return portfolioID.values[0]


class Goal(object):
    def __init__(self, name, targetYear, targetValue, initialContribution=0, monthlyContribution=0, priority=""):
        self.name = name
        self.targetYear = targetYear
        self.targetValue = targetValue
        self.initialContribution = initialContribution
        self.monthlyContribution = monthlyContribution
        if not (priority == "") and not (priority in ["Dreams", "Wishes", "Wants", "Needs"]):
            raise ValueError('Wrong value set for Priority.')
        self.priority = priority

    def getGoalProbabilities(self):
        if (self.priority == ""):
            raise ValueError('No value set for Priority.')
        lookupTable = pd.read_csv('./Data/Goal Probability Table.csv')
        match = (lookupTable['Realize'] == self.priority)
        minProb = lookupTable['MinP'][(match)]
        maxProb = lookupTable['MaxP'][(match)]
        return minProb.values[0], maxProb.values[0]
