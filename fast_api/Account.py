
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


class TransactionType():
  def __init__(self, value: str):
    if not value in("BUY", "SELL"):
      raise ValueError("Allowed types: BUY, SELL.")
    self.value = value
  def __eq__(self, other):
      return self.value == other.value

class OrderStatus():
  def __init__(self, value: str):
    if not value in("NEW", "PENDING", "FILLED", "REJECTED"):
      raise ValueError("Allowed statuses: NEW, PENDING, FILLED, REJECTED.")
    self.value = value
  def __eq__(self, other):
      return self.value == other.value

class Order:
  def __init__(self, account: Account, goal: Goal, transactionType: TransactionType, status: OrderStatus=OrderStatus("NEW"), dollarAmount: float=0.0):
    
    self.account = account
    self.transactionType = transactionType
    self.dollarAmount = dollarAmount
    self.goal = goal
    self.status = status

# pip install pandas_market_calendars


