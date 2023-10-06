import Account
#import Goal
# import TransactionType

class OrderStatus(object):
    def __init__(self, value: str):
        if not value in ("NEW", "PENDING", "FILLED", "REJECTED"):
            raise ValueError("Allowed statuses: NEW, PENDING, FILLED, REJECTED.")
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class Order(object):
    def __init__(self, account: Account, goal: Goal, transactionType: TransactionType,
                 status: OrderStatus = OrderStatus("NEW"), dollarAmount: float = 0.0):

        self.account = account
        self.transactionType = transactionType
        self.dollarAmount = dollarAmount
        self.goal = goal
        self.status = status

    def checkAccountStatus(self) -> bool:
        if self.account.accountStatus == AccountStatus("APPROVED"):
            return True
        else:
            return False

    def checkOrderSize(self) -> bool:
        if self.dollarAmount > 1.00:
            return True
        else:
            return False

    def checkBalances(self) -> bool:
        if self.transactionType == TransactionType("BUY") and self.account.cashBalance >= self.dollarAmount:
            return True
        elif self.transactionType == TransactionType("SELL"):
            goalValue = 0.0
            for allocation in self.goal.portfolio.allocations:
                price = float(yf.Ticker(allocation.ticker).basic_info["previous_close"])
                goalValue += allocation.units * price
            if self.dollarAmount <= goalValue:
                return True
            else:
                return False
        else:
            return False

    def checkOrderViability(self) -> bool:
        if self.checkAccountStatus() and self.checkOrderSize() and self.checkBalances() and isMarketOpen():
            return True
        else:
            return False

    def split(self) -> list:
        splits = []
        for allocation in self.goal.portfolio.allocations:
            if (allocation.percentage > 0):
                splits.append(SplitOrder(originalOrder=self, ticker=allocation.ticker,
                                         dollarAmount=allocation.percentage * self.dollarAmount))
        return splits
