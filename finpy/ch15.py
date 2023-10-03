
class Allocation:
  def __init__(self, ticker, percentage):
    self.ticker = ticker
    self.percentage = percentage
    self.units = 0.0

class Portfolio:

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



class Goal:
  def __init__(self, name: str, targetYear: int, targetValue: float, portfolio: Portfolio=None, initialContribution: float=0, monthlyContribution: float=0, priority: str=""):
    self.name = name
    self.targetYear = targetYear
    self.targetValue = targetValue
    self.initialContribution = initialContribution
    self.monthlyContribution = monthlyContribution
    if not (priority == "") and not (priority in ["Dreams", "Wishes", "Wants", "Needs"]):
            raise ValueError("Wrong value set for Priority.")
    self.priority = priority
    self.portfolio = portfolio

  def getGoalProbabilities(self):
    if (self.priority == ""):
            raise ValueError("No value set for Priority.")
    lookupTable=pd.read_csv("./Data/Goal Probability Table.csv")
    match = (lookupTable["Realize"] == self.priority)
    minProb = lookupTable["MinP"][(match)]
    maxProb = lookupTable["MaxP"][(match)]
    return minProb.values[0], maxProb.values[0]




class AccountType():
  def __init__(self, value: str):
    if not value in("Taxable", "Roth IRA", "Traditional IRA"):
      raise ValueError("Allowed types: Taxable, Roth IRA, Traditional IRA")
    self.value = value
  def __eq__(self, other):
      return self.value == other.value

class AccountStatus():
  def __init__(self, value: str):
    if not value in("PENDING", "IN_REVIEW", "APPROVED", "REJECTED", "SUSPENDED"):
      raise ValueError("Allowed statuses: PENDING, IN_REVIEW, APPROVED, REJECTED, SUSPENDED")
    self.value = value
  def __eq__(self, other):
      return self.value == other.value

class Account():
  def __init__(self, number: str, accountType: AccountType, accountStatus: AccountStatus, cashBalance: float=0.0):
    self.goals = []
    self.number = number
    self.cashBalance = cashBalance
    self.accountType = accountType
    self.accountStatus = accountStatus

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
    
    accounts = [myAccount, myAccount2]
    
    for account in accounts:
      print("Account: " + str(account.number))
      print("Cash: " + str(account.cashBalance))
      for goal in account.goals:
        print("Portfolio: " + goal.portfolio.name)
        for allocation in goal.portfolio.allocations:
          print(allocation.ticker + ", units: " + str(allocation.units))
        print("\n")
    
    

    
    # Split/allocate back to account.goal(s).portfolio
    for index, row in newDividends.iterrows():
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


    # Learn how to calculate Fees
    # Calculate AUM today
    for account in accounts:
      print("Account: " + str(account.number))
      print("Cash: " + str(account.cashBalance))
      aum = 0.0
      for goal in account.goals:
        print("Portfolio: " + goal.portfolio.name)
        for allocation in goal.portfolio.allocations:
          price = float(yf.Ticker(allocation.ticker).basic_info["previous_close"])
          aum += price * allocation.units
      print("AUM: " + '${0:.2f}'.format(aum))
      print("\n")
    

    # Calculate fee
    feeRate = 0.001 # 10bps
    
    for account in accounts:
      print("Account: " + str(account.number))
      print("Cash: " + str(account.cashBalance))
      aum = 0.0
      for goal in account.goals:
        print("Portfolio: " + goal.portfolio.name)
        for allocation in goal.portfolio.allocations:
          for index, row in data.iterrows():
            price = row[allocation.ticker]
            aum += price * allocation.units
      aum = aum / len(data)
      fee = aum * feeRate * (num_days_in_prev_month / 365)
      print("Average AUM: " + '${0:.2f}'.format(aum))
      print("Fee: $" + str(fee))
      print("\n")
        
