import Portfolio
import Order
from TransactionType import TransactionType


class AccountType(object):
    def __init__(self, value: str):
        if not value in ("Taxable", "Roth IRA", "Traditional IRA"):
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
    def __init__(self, number: str, accountType: AccountType, accountStatus: AccountStatus, cashBalance: float = 0.0):
        self.goals = []
        self.number = number
        self.cashBalance = cashBalance
        self.accountType = accountType
        self.accountStatus = accountStatus


class Goal(object):
    def __init__(self, name: str, targetYear: int, targetValue: float, portfolio: Portfolio = None,
                 initialContribution: float = 0, monthlyContribution: float = 0, priority: str = ""):
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
        lookupTable = pd.read_csv("./Data/Goal Probability Table.csv")
        match = (lookupTable["Realize"] == self.priority)
        minProb = lookupTable["MinP"][(match)]
        maxProb = lookupTable["MaxP"][(match)]
        return minProb.values[0], maxProb.values[0]

# pip install pandas_market_calendars
