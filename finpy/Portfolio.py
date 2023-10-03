
class Portfolio:

  def __init__(self, tickerString: str, expectedReturn: float, portfolioName: str, riskBucket: int):

    self.name = portfolioName
    self.riskBucket = riskBucket
    self.expectedReturn = expectedReturn
    self.allocations = []
    self.needRebalancing = False

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
    data = data.iloc[:, data.columns.get_level_values(1)=="Close"]
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
    allocationLookupTable=pd.read_csv('./Data/Risk Mapping Lookup.csv')
    matchTol = (allocationLookupTable['Tolerance_min'] <= riskToleranceScore) & (allocationLookupTable['Tolerance_max'] >= riskToleranceScore)
    matchCap = (allocationLookupTable['Capacity_min'] <= riskCapacityScore) & (allocationLookupTable['Capacity_max'] >= riskCapacityScore)
    portfolioID = allocationLookupTable['Portfolio'][(matchTol & matchCap)]
    return portfolioID.values[0]

  def calculateDiffsToModel(self) -> list:
    allocations = [obj.percentage for obj in self.allocations]
    holdings = [obj.units for obj in self.allocations]
    if sum(holdings) == 0.0:
      return []
    market_values = []
    for allocation in self.allocations:
      price = float(yf.Ticker(allocation.ticker).basic_info["previous_close"])
      market_values.append(price)

    current_allocation = []
    for i in range(len(holdings)):
        current_allocation.append(holdings[i] * market_values[i])
    current_allocation = [x / sum(current_allocation) for x in current_allocation]

    diff = [x1 - x2 for (x1, x2) in zip(allocations, current_allocation)]
    return diff



  def checkNeedRebalancing(self, thres: float, diff: list=[]):
    if diff == []:
      diff = self.calculateDiffsToModel()
    drift = self.calculateDrift(diff)

    if drift >= thres:
      self.needRebalancing = True
    else:
      self.needRebalancing = False

  def calculateDrift(self, diff: list=[]) -> float:
    if diff == []:
      diff = self.calculateDiffsToModel()
    return(np.abs(diff).sum()/2)




  def rebalance(self, diff: list=[]) -> list:
    if diff == []:
      diff = self.calculateDiffsToModel()

    if not self.needRebalancing:
      return []

    splitOrders = []
    for i in range(len(diff)):
        if diff[i] > 0:
            diffValue = diff[i] * holdings[i] * market_values[i]
            newOrder = Order(account = myAccount,
                                goal = myGoal,
                                transactionType = TransactionType('BUY'),
                                dollarAmount = diffValue)
            splitOrders.append(SplitOrder(originalOrder = newOrder,
                                          ticker = myPortfolio.allocations[i].ticker,
                                          dollarAmount = diffValue))
        elif diff[i] < 0:
            diffValue = abs(diff[i]) * holdings[i] * market_values[i]
            newOrder = Order(account = myAccount,
                                goal = myGoal,
                                transactionType = TransactionType('SELL'),
                                dollarAmount = diffValue)
            splitOrders.append(SplitOrder(originalOrder = newOrder,
                                          ticker = myPortfolio.allocations[i].ticker,
                                          dollarAmount = diffValue))
    return splitOrders


class SplitOrder:
  def __init__(self, originalOrder: Order, ticker: str, dollarAmount: float):

    self.originalOrder = originalOrder
    self.ticker = ticker
    self.dollarAmount = dollarAmount
    self.units = 0


if __name__ == '__name__':
    myPortfolio = Portfolio("VTI TLT IEI GLD DBC", expectedReturn = 0.05, portfolioName = "Moderate", riskBucket = 3)
    myGoal = Goal(name="Vacation", targetYear=2027, targetValue=10000, priority="Dreams", portfolio=myPortfolio)
    myAccount=Account(number="123456789", accountType="Taxable", accountStatus=AccountStatus("APPROVED"), cashBalance=11.0)
    myAccount.goals.append(myGoal)
    
    # Manual update using Chapter 12 outputs:
    myPortfolio.allocations[0].units = 0.0
    myPortfolio.allocations[1].units = 0.02213974051911262
    myPortfolio.allocations[2].units = 0.02171626612838836
    myPortfolio.allocations[3].units = 0.0163863407640173
    myPortfolio.allocations[4].units = 0.009743440233

    myPortfolio2 = Portfolio("VTI TLT IEI GLD DBC", expectedReturn = 0.03, portfolioName = "Conservative", riskBucket = 2)
    myGoal2 = Goal(name="Car", targetYear=2025, targetValue=5000, priority="Dreams", portfolio=myPortfolio2)
    myAccount2=Account(number="987654321", accountType="Taxable", accountStatus=AccountStatus("APPROVED"), cashBalance=21.0)
    myAccount2.goals.append(myGoal2)
    
    # Manual update using Chapter 12 outputs:
    myPortfolio2.allocations[0].units = 0.019070282760887385
    myPortfolio2.allocations[1].units = 0.0
    myPortfolio2.allocations[2].units = 0.10911027337161164
    myPortfolio2.allocations[3].units = 0.019273081685982695
    myPortfolio2.allocations[4].units = 0.0

    myPortfolio.calculateDrift()
    myPortfolio.calculateDiffsToModel()

    splits = myPortfolio.rebalance()
